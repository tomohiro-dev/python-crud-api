from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

# ログの設定
logging.basicConfig(level=logging.DEBUG)

# サンプルデータ
books = {
    1: {'id': 1, 'name': 'Taro Tanaka', 'email': 'tarotanaka@test.test'},
    2: {'id': 2, 'name': 'Jiro Jinbo', 'email': 'jirojinbo@test.test'}
}

# getメソッド
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# 特定の本をIDを通して取得する
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = books.get(book_id)
    if book:
        return jsonify({book_id: book})
    return {'error': '本が見つかりません'}, 404

# Createメソッド
@app.route('/books', methods=['POST'])
def create_book():
    # 新規作成時に既存idの最大数に1を追加する
    new_book = {
        'id': len(books)+1,
        'name': request.json['name'],
        'email': request.json['email']
    }
    books[new_book['id']] = new_book
    return jsonify(new_book), 201

# Updateメソッド
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = books.get(book_id)
    if book:
        book['name']=request.json.get('name', book['name'])
        book['email']=request.json.get('email', book['email'])
        return jsonify(book)
    return jsonify({'error': '本が見つかりません'}), 404

# Deleteメソッド
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    if book_id in books:
        del books[book_id]
        return jsonify({'data': '本の削除が成功しました'})
    return jsonify({'error': '本が見つかりません'}), 404


    
if __name__ == '__main__':
    app.run(debug=True)