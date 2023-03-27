from flask import Flask, request, jsonify
import qrcode
from io import BytesIO
import base64


app = Flask(__name__)

@app.route('/generate-price-tags', methods=['POST'])
def generate_price_tags():
    data = request.get_json()
    # Генерация ценников на основе данных из JSON
    products = data
    price_tags = ""
    for product in products:
        category = product['category']
        name = product['name']
        description = product['description']
        monthly_payment = product['monthly_payment']
        qr_link = product['qr_link']
        months = product['months']
        discount_percentage = product['discount_percentage']
        total_amount = product['total_amount']
        date = product['date']

        # qr_link_2 = product['qr_link_2']
        # qr_link_3 = product['qr_link_3']
        # qr_codes = []
        # for qr_product in [qr_link, qr_link_2, qr_link_3]:
        #     qr_code = qr_product
        #     # Создание QR-кода в виде изображения
        #     qr = qrcode.QRCode(version=1, box_size=10, border=5)
        #     qr.add_data(qr_code)
        #     qr.make(fit=True)
        #     img = qr.make_image(fill_color="black", back_color="white")
        #     # Преобразование изображения в строку base64
        #     buffered = BytesIO()
        #     img.save(buffered, format="PNG")
        #     img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
        #     qr_codes.append(img_str)

                
        # Создание QR-кода в виде изображения
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(qr_link)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color=(218, 218, 218))
        # Преобразование изображения в строку base64
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
        if monthly_payment:
            tag = f"""
                <div class="tag">
                    <div class="category">{category['ru']}</div>
                    <div class="title">{name.upper()}</div>
                    <div class="description">{description}</div>

                    <div class="dash"></div>

                    <div class="installment_plan">В рассрочку:</div>
                    <div class="monthly_payment">{monthly_payment} сум</div>
                    <div class="months">На {months} месяца</div>

                    <div class="dash"></div>

                    <div class="footer">
                        <img src="data:image/png;base64,{img_str}" alt="qr-code-товар" class="footer_img" />

                        <div class="total_amount_24">
                            <div class="total_amount_24_text">Полная сумма</div>
                            <div class="total_amount_24_percentage">{discount_percentage['first']}</div>
                            <div class="total_amount_24_price">{total_amount['first']} сум</div>
                        </div>
                        
                        <div class="total_amount_12">
                            <div class="total_amount_12_text">0-0-12</div>
                             <div class="total_amount_12_percentage">{discount_percentage['second']}</div>
                            <div class="total_amount_12_price">{total_amount['second']}</div>
                        </div>

                    </div>

                    <div class="date">
                        Дата: {date}
                    </div>

                    <div class="dash"></div>

                </div>

                <div class="tag">
                    <div class="category">{category['uz']}</div>
                    <div class="title">{name.upper()}</div>
                    <div class="description">{description}</div>

                    <div class="dash"></div>

                    <div class="installment_plan">Muddatli to'lovga:</div>
                    <div class="monthly_payment">{monthly_payment} so'm</div>
                    <div class="months">{months} oyga</div>

                    <div class="dash"></div>

                    <div class="footer">
                        <img src="data:image/png;base64,{img_str}" alt="qr-code-товар" class="footer_img" />
                   
                        <div class="total_amount_24">
                            <div class="total_amount_24_text_uz">To'liq to'lov</div>
                            <div class="total_amount_24_percentage">{discount_percentage['first']}</div>
                            <div class="total_amount_24_price">{total_amount['first']} so'm</div>
                        </div>
                        
                        <div class="total_amount_12">
                            <div class="total_amount_12_text">0-0-12</div>
                             <div class="total_amount_12_percentage">{discount_percentage['second']}</div>
                            <div class="total_amount_12_price">{total_amount['second']}</div>
                        </div>

                    </div>

                    <div class="date">
                        Sana: {date}
                    </div>

                    <div class="dash"></div>

                </div>

            """
        else:
            tag = f"""
                <div class="tag">
                    <div class="category">{category['ru']}</div>
                    <div class="title">{name.upper()}</div>
                    <div class="description">{description}</div>

                    <div class="dash"></div>

                    <div class="installment_plan">В рассрочку:</div>
                    <div class="monthly_payment">{monthly_payment} сум</div>
                    <div class="months">На {months} месяца</div>

                    <div class="dash"></div>

                    <div class="footer">
                        <img src="data:image/png;base64,{img_str}" alt="qr-code-товар" class="footer_img" />

                        <div class="total_amount_24">
                            <div class="total_amount_24_text">Полная сумма</div>
                            <div class="total_amount_24_percentage">{discount_percentage['first']}</div>
                            <div class="total_amount_24_price">{total_amount['first']} сум</div>
                        </div>
                        
                        <div class="total_amount_12">
                            <div class="total_amount_12_text">0-0-12</div>
                             <div class="total_amount_12_percentage">{discount_percentage['second']}</div>
                            <div class="total_amount_12_price">{total_amount['second']}</div>
                        </div>

                    </div>

                    <div class="date">
                        Дата: {date}
                    </div>

                    <div class="dash"></div>

                </div>

                <div class="tag">
                    <div class="category">{category['uz']}</div>
                    <div class="title">{name.upper()}</div>
                    <div class="description">{description}</div>

                    <div class="dash"></div>

                    <div class="installment_plan">Muddatli to'lovga:</div>
                    <div class="monthly_payment">{monthly_payment} so'm</div>
                    <div class="months">{months} oyga</div>

                    <div class="dash"></div>

                    <div class="footer">
                        <img src="data:image/png;base64,{img_str}" alt="qr-code-товар" class="footer_img" />
                   
                        <div class="total_amount_24">
                            <div class="total_amount_24_text_uz">To'liq to'lov</div>
                            <div class="total_amount_24_percentage">{discount_percentage['first']}</div>
                            <div class="total_amount_24_price">{total_amount['first']} so'm</div>
                        </div>
                        
                        <div class="total_amount_12">
                            <div class="total_amount_12_text">0-0-12</div>
                             <div class="total_amount_12_percentage">{discount_percentage['second']}</div>
                            <div class="total_amount_12_price">{total_amount['second']}</div>
                        </div>

                    </div>

                    <div class="date">
                        Sana: {date}
                    </div>

                    <div class="dash"></div>

                </div>

            """

        price_tags += tag

    # Запись HTML-кода в файл
    with open('price-tags.html', 'w', encoding='utf-8') as file:
        file.write(f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>Ценники</title>
                <link rel="stylesheet" href="styles.css">
            </head>
            <body>
                <div id="price-tags">{price_tags}</div>
            </body>
            </html>
        """)
    return jsonify({'result': 'success'})

if __name__ == '__main__':
    app.run()