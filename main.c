#include "stm32f4xx.h"
#define PGout(x)    *(unsigned int *)(PERIPH_BB_BASE+((unsigned int)(&GPIOG->ODR)-PERIPH_BASE)*32+x*4)

static GPIO_InitTypeDef GPIO_InitStructure;

void delay(void)
{
	uint32_t i=0x2000000;
	
	while(i--);
}
/*

#define GPIOF               ((GPIO_TypeDef *) GPIOF_BASE)
#define GPIOF_BASE            (AHB1PERIPH_BASE + 0x1400)
#define AHB1PERIPH_BASE       (PERIPH_BASE + 0x00020000)
#define PERIPH_BASE           ((uint32_t)0x40000000) < Peripheral base address in the alias region       
#define PERIPH_BB_BASE        ((uint32_t)0x42000000) < Peripheral base address in the bit-band region   
*/

int main(void)
{
	//ʹ��(��)�˿�G��Ӳ��ʱ�ӣ����ǶԶ˿�F����
	RCC_AHB1PeriphClockCmd(RCC_AHB1Periph_GPIOG, ENABLE);


	//��ʼ��GPIO����
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_11;		//��11������
	GPIO_InitStructure.GPIO_Mode= GPIO_Mode_OUT;	//���ģʽ
	GPIO_InitStructure.GPIO_OType = GPIO_OType_PP;	//��������������������������
	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_100MHz;//������Ӧ
	GPIO_InitStructure.GPIO_PuPd = GPIO_PuPd_NOPULL;	//û��ʹ������������

	GPIO_Init(GPIOG,&GPIO_InitStructure);
	
	
	while(1)
	{
		//PG9��������ߵ�ƽ
		//GPIO_SetBits(GPIOG,GPIO_Pin_11);
		PGout(11)=1;
		delay();
		
		//PG9��������͵�ƽ
		//GPIO_ResetBits(GPIOG,GPIO_Pin_11);
		PGout(11)=0;
		delay();	
	}



}
