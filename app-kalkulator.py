from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/send', methods=['POST'])
def send(sum=sum):
    if request.method == 'POST':
        matematika = request.form['matematika']
        matematika2 = request.form['matematika2']
        operasi = request.form['operasi']

        if operasi == 'penjumlahan':
            sum = float(matematika) + float(matematika2)
            return render_template('index.html', sum=sum)

        elif operasi == 'pengurangan':
            sum = float(matematika) - float(matematika2)
            return render_template('index.html', sum=sum)

        elif operasi == 'perkalian':
            sum = float(matematika) * float(matematika2)
            return render_template('index.html', sum=sum)

        elif operasi == 'pembagian':
            sum = float(matematika) / float(matematika2)
            return render_template('index.html', sum=sum)
        else:
            return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
