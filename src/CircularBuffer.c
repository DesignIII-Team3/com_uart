/*
 * CircularBuffer.c
 *
 *  Created on: 16 nov. 2022
 *      Author: sebri
 */

#include "CircularBuffer.h"

volatile unsigned int item_in_buffer = 0;

int CBuffer_write(uint8_t p_data)
{
	if(item_in_buffer >= BUFFER_SIZE) return 0;

	circular_buffer[buffer_head] = p_data;		// mettre data dans le buffer

	buffer_head++;								// incrementer pos head
	item_in_buffer++;

	if(buffer_head >= BUFFER_SIZE){				// si tete = ou > que taille buffer
		buffer_head = 0;						// alors retour a 0
	}

	return 1;
}

int CBuffer_read(uint8_t* r_data)
{
	if(CBuffer_isEmpty()) return 0;				// retourne 0 si buffer est vide

	*r_data = circular_buffer[buffer_queue];	// mettre valeur a pos head dans r_data

	buffer_queue++;								// incrementer pos queue
	item_in_buffer--;

	if(buffer_queue >= BUFFER_SIZE){			// si tete = ou > que taille buffer
		buffer_queue = 0;						// alors retour a 0
	}

	return 1;
}

int CBuffer_isEmpty()
{
	return buffer_head == buffer_queue;
}
