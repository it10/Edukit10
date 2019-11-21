# Pinout Multiconector Edukit10

|Pin 	|	Función                  |  Arduino      |
|-----|--------------------------|---------------|		
| 1		    |		Digital/pwm	       |	D11
| 2		    |		Analógico, Digital |	A0
| 3		    |	  Analógico, Digital |  A1
| 4		    |	  Digital/pwm			   |  D10	
| 5		    |   Digital/pwm        |  D9
| 6		    |	  Digital/pwm			   |  D6
|	7		    |		Analógico/i2c SDA	 |  A4
|	8	      |   Analógico/i2c SCL  |  A5
| VCC (9) |   VCC, Entrada Reg   | 	Vin
| GND(10)	|   GROUND		         | GND
| +5v(11) |   Salida Reg Volt.   | +5V
|N/A(12)	|		Pin ciego          | N/A
-------------------------------------------------|



## Esquema

          
         ---	  ---       |
    N/A	| o |  | o | 1		|	1-	Digital/pwm		        D11
         ---	  ---    		|
    +5v	| o |  | o | 2		|	2-	Analógico, Digital		A0
         ---    ---		    |
    GND	| o |  | o | 3		|	3-      Analógico, Digital      	A1
         ---    ---		    |
    Vcc	| o |  | o | 4		|	4-	Digital/pwm			D10	
         ---    ---		    |		
     8	| o |  | o | 5		|	5-      Digital/pwm             	D9
	       --- 	---		|			
     7	| o |  | o | 6		|	6-	Digital/pwm			D6
	       ---    ---		    |	
	 			                  |	7-	Analógico/i2c SDA		A4
            * VCC(9)			|	
            GND(10)			|	8-	Analógico/i2c SCL       	A5
            N/A(12)			|
           +5v(11)			|	9-	VCC, Entrada Reg        	Vin


