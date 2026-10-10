#!python3
import typing
import random

def gen_event():
    names: list[str] = [
            "Thorin", "Balin", "Dwalin",
            "Fili", "Kili", "Oin", "Víli", "Thrainor",
            "Gloin", "Dori", "Nori", "Ori",  "Kazad",
            "Bifur", "Bofur", "Bombur", "Dain", "Rurik",
            "Thrain", "Thror", "Durin", "Fundin", "Thráin",
            "Nain", "Dís", "Gimli", "Telchar", "Azaghal",
            "Narvi", "Flói", "Frár", "Lóni", "Náli",
            "Yarvi", "Borin", "Darin", "Grorin", "Bromdar",
            "Bardin", "Gundar", "Khurin", "Durgin",
            "Fundar", "Gróin", "Nár", "Frerin", "Khardin",
            "Mundar", "Thrákur", "Tharkun",
        ]
    actions: list[str] = [
            "correr", "martelar", "minerar", "beber pinga", 
            "rir alto", "forjar armas", "escavar túneis", 
            "brandir o machado", "bater com o martelo", "polir ouro",
            "lapidar gemas", "fundir metal", "cantar canções antigas",
            "contar histórias", "desafiar um elfo", "comer carne assada",
            "devorar pão", "roubar uma cerveja", "arrotar na taverna",
            "dormir sobre ouro", "guardar tesouros", "proteger Erebor",
            "explorar cavernas",
            "enfrentar um troll",
            "lutar contra orcs",
            "afiar o machado",
            "reparar armaduras",
            "fabricar anéis",
            "carregar minério",
            "empurrar carrinhos",
            "dinamitar rochas",
            "procurar mithril",
            "negociar joias",
            "regatear preços",
            "apostar moedas",
            "jogar dados",
            "dançar na taverna",
            "tocar tambor",
            "cantar fora do tom",
            "roncar como um dragão",
            "reclamar dos elfos",
            "insultar um orc",
            "desafiar o rei",
            "esconder uma cerveja",
            "disputar queda de braço",
            "fazer flexões",
            "exibir a barba",
            "pentear a barba",
            "tropeçar numa bigorna",
            "dormir durante a reunião",
        ]
    while True:
        hero: dict[str, str] =  []
        name = names[random.randint(0, len(names) - 1)]
        action = actions[random.randint(0, len(actions) - 1)]
        hero = [name, action]
        yield hero


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===\n")
    i = 0
    gen = gen_event()
    while i < 999:
        print(f"Event {i}: {next(gen)[0]} did action {next(gen)[1]}")
        i += 1
