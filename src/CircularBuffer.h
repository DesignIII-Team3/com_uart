/*
 * CircularBuffer.h
 *
 *  Created on: 16 nov. 2022
 *      Author: sebri
 */

#ifndef CIRCULARBUFFER_H_
#define CIRCULARBUFFER_H_

#include <stdint.h>

#define BUFFER_SIZE 20

uint8_t circular_buffer[BUFFER_SIZE];
volatile unsigned int buffer_head;
volatile unsigned int buffer_queue;

volatile unsigned int item_in_buffer;

/**
 * Ecrit une donnee dans le buffer circulaire
 * et retourne 1 en cas de succes
 */
int CBuffer_write(uint8_t p_data);

/**
 * Lit la donnee a la tete du buffer et met la valeur
 * dans le pointeur de retour
 * retourne 1 en cas de succes
 */
int CBuffer_read(uint8_t* r_data);

/**
 * REtourne 1 si le buffer est vide
 */
int CBuffer_isEmpty();

#endif /* CIRCULARBUFFER_H_ */
