/*
 * uart.h
 *
 *  Created on: 15 nov. 2022
 *      Author: andrea
 */

#ifndef UART_H_
#define UART_H_

#define SIZE_CIRCULAR_BUFFER 20

/**
 * Configurer le uart1
 */
void uart_configure();

/**
 * Configurer les interruptions pour le Uart1
 */
void USART1_IRQHandler();

int uart_sendString(char* p_str);

int uart_sendCommande(uint8_t p_cmd,
		 	 	 	  void* p_data,
					  unsigned int p_size);



#endif /* UART_H_ */
