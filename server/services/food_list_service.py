from server.config.database import Conexao

db = Conexao()


def get_food_list():
    datas = []
    query = "SELECT * FROM public.food_list where status is not false order by created_at desc"
    lista = db.consultar(query)
    for item in lista:
        data = {
            "id": item[0],
            "name": item[1],
            "type": item[2],
            "amount": item[3],
            "created_at": item[5]
        }
        datas.append(data)

    return datas


def add_to_food_list(item):
    if item['food_type'] not in ['Proteina', 'Carboidrato', 'Gordura']:
        return "Tipo alimento invalido."
    else:
        query = f"INSERT INTO public.food_list (nome, tipo, quantidade, created_at, updated_at) VALUES('{item['food_name']}', '{item['food_type']}', {item['food_amount']}, now(), now());"
        data = db.manipular(query)
        return data


def delete_item_to_food_list(id):
    query = f"UPDATE public.food_list SET status=false, updated_at='now()' WHERE id={id};"

    if db.manipular(query):
        return f"ID: {id} removido com sucesso!"
    else:
        return f"Erro ao remover ID: {id}!"


def get_graph_to_food_list():
    query = f"SELECT * FROM public.food_list where status is not false"
    data = db.consultar(query)
    tp_gordura = 0
    tp_carbo = 0
    tp_protein = 0
    for item in data:
        if item[2] == 'Proteina':
            tp_protein += 1
        elif item[2] == 'Gordura':
            tp_gordura += 1
        else:
            tp_carbo += 1

    return {"carboidrato": tp_carbo, "gordura": tp_gordura, "proteina": tp_protein}


def get_list_by_date_to_food_list(date):
    datas = []
    query = f"select * from food_list where created_at <= '{date}'"
    list = db.consultar(query)
    for item in list:
        data = {
            "id": item[0],
            "name": item[1],
            "type": item[2],
            "amount": item[3],
            "created_at": item[5]
        }
        datas.append(data)

    return datas

