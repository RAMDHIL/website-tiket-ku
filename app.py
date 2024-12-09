from flask import Flask ,render_template, request,redirect
from datetime import datetime
import random
app = Flask(__name__);

product = [
        {
            "id": 1,
            "nama":"argo parahyangan",
            "jurusan":"gambir - bandung",
            "harga":2500000
        }, 
        {   
            "id": 2,
            "nama":"argo bromo anggrek",
            "jurusan":"gambir - surabaya pasar turi",
            "harga":650000    
        },
        {
            "id": 3,
            "nama":"argo sindoro",
            "jurusan":"gambir - semarang",
            "harga":500000
        },
         {
            "id": 4,
            "nama": "Bus Lorena",
            "jurusan": "Jakarta - Semarang",
            "harga": 250000
        },
        {
            "id": 5,
            "nama": "Bus Primajasa",
            "jurusan": "Bandung - Tasikmalaya",
            "harga": 90000
        },
        {
            "id": 6,
            "nama": "Bus Gunung Harta",
            "jurusan": "Denpasar - Banyuwangi",
            "harga": 350000
        },
        {
            "id": 7,
            "nama": "Wings Air",
            "jurusan": "Bali - Lombok",
            "harga": 600000
        },
        {
            "id": 8,
            "nama": "Super Air Jet",
            "jurusan": "Bandung - Medan",
            "harga": 1300000
        },
        {
            "id": 9,
            "nama": "NAM Air",
            "jurusan": "Balikpapan - Manado",
            "harga": 1400000
        },
]
@app.route('/home-tiketku',methods=['GET'])
def home():
    

    return render_template('home.html', products=product)

@app.route('/about-tiketku',methods=['GET'])
def about():
    return render_template('about.html')


@app.route('/penumpang/<int:id>',methods=['GET'])
def buy(id):
    for p in product:
        if int(id) == p['id']:
            nama = p['nama']
            harga = p['harga']
            jurusan = p['jurusan']
    
    return render_template("penumpang.html", nama=nama,harga=harga,jurusan=jurusan,id=id)

@app.route('/payment/<int:id>',methods=['POST'])   
def payment(id):
    jumlahtiket = request.form.get('jumlahtiket')
    nama_pembeli_tiket = request.form.get('nama')
    random_number = random.randint(10**9, 10**10 - 1)
    jumlahtiket = int(jumlahtiket);
    
    for p in product:
        if id == p['id']:
            currenttime = datetime.now()
            tanggal = currenttime.strftime('%Y-%m-%d %H:%M:%S')
            nama = p['nama']
            jurusan = p['jurusan'] 
            harga = p['harga']
            result = harga * jumlahtiket 
            
    result = "{:,.0f}".format(result).replace(",", ".")
    return render_template('invoice.html',nama_pembeli_tiket=nama_pembeli_tiket,harga=harga, jurusan=jurusan,tanggal=tanggal,nama=nama,jumlahtiket=jumlahtiket,result=result,va=random_number);
   
@app.route('/invoice',methods=['GET'])
def invoice():
    return render_template('inovice.html')



if __name__ == '__main__':
    app.run(debug=True)