from flask import Flask, jsonify, request
from http import HTTPStatus

app = Flask(__name__)

greenHouseS = [
    {
        'id': 1,
        'name': 'Charmgarden',
        'description': 'place of the best lettuce'
    },
    {
        'id': 2, 
        'name': 'cottageshine',
        'description': 'the house top garden of tomato'
    }
]


@app.route('/greenHouseS', methods=['GET']) #list every ghs
def get_greenHouseS():
    return jsonify({'data': greenHouseS})


@app.route('/greenHouseS/<int:greenHouseID>', methods=['GET'])
def get_greenHouse(greenHouseID):
    greenHouse = next((greenHouse for greenHouse in greenHouseS if greenHouse['id'] == greenHouseID), None)

    if greenHouse:
        return jsonify(greenHouse)

    return jsonify({'message': 'greenHouse not found'}), HTTPStatus.NOT_FOUND


@app.route('/greenHouseS', methods=['POST']) #post A new record
def create_greenHouse():
    data = request.get_json()

    name = data.get('name')
    description = data.get('description')

    greenHouse = {
        'id': len(greenHouseS) + 1, #overrides if sent
        'name': name,
        'description': description
    }

    greenHouseS.append(greenHouse)

    return jsonify(greenHouse), HTTPStatus.CREATED


@app.route('/greenHouseS/<int:greenHouseID>', methods=['PUT'])
def update_greenHouse(greenHouseID):
    greenHouse = next((greenHouse for greenHouse in greenHouseS if greenHouse['id'] == greenHouseID), None)

    if not greenHouse:
        return jsonify({'message': 'greenHouse not found'}), HTTPStatus.NOT_FOUND

    data = request.get_json()

    greenHouse.update(
        {
            'name': data.get('name'),
            'description': data.get('description')
        }
    )

    return jsonify(greenHouse)

@app.route('/greenHouseS/<int:greenHouseID>', methods=['DELETE'])
def delete_greenHouse(greenHouseID):
     greenHouse = next((greenHouse for greenHouse in greenHouseS if greenHouse['id'] == greenHouseID), None)
     if not greenHouse:
        return jsonify({'message': 'greenHouse not found'}), HTTPStatus.NOT_FOUND
     greenHouseS.remove(greenHouse)
     return '', HTTPStatus.NO_CONTENT

@app.route("/")###########notneeded#####
def hello():###########notneeded#####
    return "Hello Weeorld!"###########notneeded#####


if __name__ == '__main__':
    app.run(host='localhost', port=5000)