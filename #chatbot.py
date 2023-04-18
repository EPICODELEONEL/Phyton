#chatbot
veicolo_offerta = "bici elettrica"
prezzo_offerta = 19.90
biciclette = ['mountain bike', 'Graziella', 'BMX', 'olandesina', 'monociclo']
motociclette = ['motocross', 'Harley', 'chopper','Il Ciao']
veicoli = []
ANNO_ATTUALE = 2023

print('Benvenuto al noleggio EpicBikes! ')
print(f"Non perderti l'offerta sulla {veicolo_offerta} al prezzo di {prezzo_offerta}")

print('Inserisci il tuo anno di nascita: ')

anno_nascita = int(input())
anni_cliente = ANNO_ATTUALE - anno_nascita

print(f'La tua età è {anni_cliente} anni')

if anni_cliente < 18:
    print('Sei minorenne')
    veicoli = biciclette
else:
    print('Sei minorenne')
    veicoli = biciclette + motociclette

