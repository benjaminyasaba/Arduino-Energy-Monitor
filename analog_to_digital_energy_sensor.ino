#include <LiquidCrystal.h>

/* * HARDWARE INTEGRATION:
 * The LiquidCrystal library handles the 4-bit data protocol.
 * Mapping (RS, E, D4, D5, D6, D7) to Arduino pins 7-12.
 */
LiquidCrystal lcd(7, 8, 9, 10, 11, 12);

// Constant for the Analog-to-Digital Converter (ADC) resolution
const float ADC_RESOLUTION = 1023.0; 

// Pin for the B103 Potentiometer (Wiper/Middle Pin)
const int sensorPin = A0; 

void setup() {
  // Initialize LCD: 16 columns, 2 rows
  lcd.begin(16, 2);
  
  // Start Serial at 9600 baud for Python data logging [cite: 26, 28]
  Serial.begin(9600); 
  
  lcd.print("Energy Monitor");
  delay(2000); // Allow system to stabilize
  lcd.clear();
}

void loop() {
  /*
   * DATA ACQUISITION:
   * analogRead turns 0-5V into a digital integer (0-1023).
   */
  int rawValue = analogRead(sensorPin);
  
  /*
   * SIGNAL PROCESSING:
   * 1. Convert the raw digital value to a float ratio.
   * 2. Map that ratio to a simulated 15.0 Amp current draw.
   */
  float current = (rawValue / ADC_RESOLUTION) * 15.0;
  
  /*
   * CIRCUIT MATH (P = V * I):
   * Assuming a constant standard voltage of 120V.
   */
  float power = 120.0 * current;

  // DISPLAY LOGIC: Row 0 (Current)
  lcd.setCursor(0, 0);
  lcd.print("Current: "); 
  lcd.print(current, 2); // 2 decimal places for precision
  lcd.print("A");
  
  // DISPLAY LOGIC: Row 1 (Power)
  lcd.setCursor(0, 1);
  lcd.print("Power:   "); 
  lcd.print(power, 1);   // 1 decimal place (Watts)
  lcd.print("W");

  /*
   * DATA OUTPUT:
   * Printing as a Comma-Separated Value (CSV) for your Python script.
   */
  Serial.print(current);
  Serial.print(",");
  Serial.println(power);

  delay(500); // Sampling rate of 2Hz (twice per second)
}