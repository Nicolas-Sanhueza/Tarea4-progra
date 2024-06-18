#include <ArduinoJson.h>
#include <CTBot.h>

CTBot CasaPlaya;

static const int Entrada = 12;
static const int Cocina = 13;
static const int Dormitorio = 14;
static const int Piscina = 26;
static const int Bano = 27;

const char* ssid = "Tomas_Pixel";
const char* password = "olaolaola";

#define TokenBot "6779162023:AAHmGcOa4GuYvgMxld_7JvRtj2PuFMYDh0E"
#define ChatID 6784019294

void setup() {
  Serial.begin(115200);

  pinMode(Entrada, OUTPUT);
  pinMode(Cocina, OUTPUT);
  pinMode(Dormitorio, OUTPUT);
  pinMode(Piscina, OUTPUT);
  pinMode(Bano, OUTPUT);

  CasaPlaya.wifiConnect(ssid, password);
  CasaPlaya.setTelegramToken(TokenBot);

  if (CasaPlaya.testConnection()) {
    Serial.println("WiFi conectado.");
  }
  CasaPlaya.sendMessage(ChatID, "¿Que desea Maestro?");
}

void loop() {
  TBMessage MensajeUsuario;

  if (CTBotMessageText == CasaPlaya.getNewMessage(MensajeUsuario)) {

    if (MensajeUsuario.text == "/Prender entrada") {
      digitalWrite(Entrada, HIGH);
      CasaPlaya.sendMessage(ChatID, "Luz de entrada encendida");                      
    }
  }
}
