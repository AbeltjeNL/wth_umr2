# WTH UMR2 Regulator Integratie voor Home Assistant

![WTH Logo](custom_components/wth_umr2/logo.png)

**Versie:** 1.0  
**Auteur:** AbeltjeNL  
**Licentie:** MIT

Deze custom component integreert de WTH UMR2 verwarmingsregulator met Home Assistant, waarmee u uw verwarmingssysteem kunt monitoren en beheren.

## Functies

- **GUI Configuratie**: Eenvoudige installatie via de Home Assistant UI
- **Uitgebreide Monitoring**: Toegang tot alle datapunten van de WTH UMR2
- **Real-time Updates**: Haalt elke 30 seconden de huidige status op
- **Meerdere Sensoren**: Meer dan 60 sensor entiteiten voor:
  - Hoofdsysteem status en modus
  - Thermostaat status en temperaturen (8 zones)
  - Kleppen posities (10 kleppen)
  - Verwarmer en koeler outputs
  - Pomp snelheid
  - Temperatuur sensoren (10 sensoren)
  - Communicatie status (Fanlink, RF, Modbus, Bluetooth, Ethernet)
  - Aangesloten apparaten

## Installatie

### Handmatige Installatie

1. Kopieer de `custom_components/wth_umr2` map naar de `custom_components` map van uw Home Assistant
2. Als de `custom_components` map niet bestaat, maak deze aan in uw Home Assistant configuratie map
3. Herstart Home Assistant

## Configuratie

1. Ga naar **Instellingen** → **Apparaten & Diensten**
2. Klik op **+ INTEGRATIE TOEVOEGEN**
3. Zoek naar "WTH UMR2 Regulator"
4. Voer het IP-adres van uw WTH UMR2 apparaat in (bijv. `192.168.178.69`)
5. Klik op **Verzenden**

De integratie zal automatisch alle beschikbare sensoren ontdekken en entiteiten aanmaken.

## Beschikbare Sensoren

### Hoofdstatus
- **Hoofdstatus**: Algemene systeemstatus
- **Bedrijfsmodus**: Huidige modus (verwarmen/koelen)
- **Display**: Huidige displaywaarde
- **LED Status**: LED indicator status
- **Verwarmingsfactor**: Verwarmingsfactor percentage
- **Koelingsfactor**: Koelingsfactor percentage
- **PWM Factor**: PWM regelpercentage

### Outputs
- **Verwarmer Output**: Verwarmer vermogen percentage
- **Koeler Output**: Koeler vermogen percentage
- **Pomp Snelheid**: Circulatiepomp snelheid percentage
- **Klep 1-10**: Individuele kleppen posities (0-100%)

### Thermostaten (8 zones)
- **Thermostaat 1-8**: Aan/uit status met temperatuur en setpoint attributen
- **Thermostaat 1-8 Temperatuur**: Huidige temperatuur metingen

### Inputs
- **Max Input**: Maximum temperatuur input status
- **Retour Input**: Retour temperatuur input status
- **Condens Input**: Condensatie sensor status
- **Temperatuur Sensor 1-10**: Externe temperatuur sensoren

### Communicatie
- **Fanlink Status**: Fanlink communicatie status
- **RF Status**: RF communicatie status
- **Modbus Status**: Modbus communicatie status
- **Bluetooth Status**: Bluetooth communicatie status
- **Ethernet Status**: Netwerkverbinding status met IP details
- **Fanlink Apparaat 1-10**: Aangesloten Fanlink apparaten met serienummers

## Entiteit Attributen

Veel sensoren bevatten extra attributen met gedetailleerde informatie:

- **Thermostaat sensoren**: Bevatten temperatuur, setpoint en aan/uit status
- **Communicatie sensoren**: Bevatten IP-adressen, MAC-adressen en apparaat details
- **Apparaat sensoren**: Bevatten serienummers, laatst gezien tijdstempels en apparaattypes

## Probleemoplossing

### Kan Geen Verbinding Maken
- Controleer of het IP-adres correct is
- Zorg ervoor dat de WTH UMR2 aan staat en verbonden is met uw netwerk
- Controleer of Home Assistant het apparaat kan bereiken (probeer te pingen)
- Verifieer dat de URL `http://UW_IP/get.json?f=$.status.*` geldige JSON retourneert in een browser

### Ongeldige Reactie
- Controleer of u verbinding maakt met een WTH UMR2 apparaat
- Controleer of de apparaat firmware up-to-date is
- Verifieer dat het JSON endpoint toegankelijk is

### Ontbrekende Sensoren
- Sommige sensoren verschijnen mogelijk niet als de bijbehorende hardware niet is aangesloten
- Temperatuur sensoren met nul waarden worden verborgen totdat ze echte gegevens rapporteren
- Niet alle 10 temperatuur sensoren of kleppen kunnen in gebruik zijn

## Geavanceerde Configuratie

### Polling Interval
Het standaard polling interval is 30 seconden. Om dit te wijzigen, pas `SCAN_INTERVAL` aan in `__init__.py`:

```python
SCAN_INTERVAL = timedelta(seconds=30)  # Wijzig naar uw gewenste interval
```

### Apparaat Informatie
De integratie haalt automatisch op:
- Apparaat ID
- Firmware versie
- Hardware versie
- Model informatie

## Ondersteuning

Voor problemen, functie verzoeken of bijdragen, bezoek de GitHub repository.

## Licentie

Deze integratie wordt geleverd zoals het is voor persoonlijk gebruik met WTH UMR2 verwarmingsregelaars.

## Changelog

### Versie 1.0
- Eerste release
- Volledige ondersteuning voor alle JSON datapunten
- GUI configuratie met logo ondersteuning
- Uitgebreide sensor dekking (60+ sensoren)
- Real-time updates elke 30 seconden
- Engelse en Nederlandse taal ondersteuning
- Apparaat informatie met hardware en firmware versies
- Directe configuratie URL naar apparaat web interface
