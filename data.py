from products.models import Brand, HsnCode, Product, Shoe, Style, ShoeStyle

# Step 1: Create Brands
brand1 = Brand.objects.create(name='Nike', description='Premium Sports Brand')
brand2 = Brand.objects.create(name='Adidas', description='Global Sportswear Brand')
brand3 = Brand.objects.create(name='Puma', description='German Sports Brand')
brand4 = Brand.objects.create(name='Reebok', description='Athletic Footwear Brand')

# Step 2: Create HsnCode Records
hsn1 = HsnCode.objects.create(index= 1041,item_code=12345, item_name='Shoes', item_type='Footwear', GSTe=5.00, hsn_code=640299, GST=5.00)
hsn2 = HsnCode.objects.create(index= 1042,item_code=12346, item_name='Sports Shoes', item_type='Athletic Footwear', GSTe=12.00, hsn_code=640391, GST=12.00)
hsn3 = HsnCode.objects.create(index= 1043,item_code=12347, item_name='Running Shoes', item_type='Footwear', GSTe=18.00, hsn_code=640411, GST=18.00)

# Step 3: Create Initial Product Records
product1 = Product.objects.create(name='Air Max', price_inclusive=5000, description='Nike Air Max Shoes', brand=brand1, gst_rate=hsn1.GSTe, hsn_code=hsn1.hsn_code)
product2 = Product.objects.create(name='Ultraboost', price_inclusive=8000, description='Adidas Ultraboost Shoes', brand=brand2, gst_rate=hsn2.GSTe, hsn_code=hsn2.hsn_code)
product3 = Product.objects.create(name='Ignite', price_inclusive=4500, description='Puma Ignite Shoes', brand=brand3, gst_rate=hsn1.GSTe, hsn_code=hsn1.hsn_code)
product4 = Product.objects.create(name='Classic Leather', price_inclusive=6000, description='Reebok Classic Leather Shoes', brand=brand4, gst_rate=hsn2.GSTe, hsn_code=hsn2.hsn_code)

# Step 4: Create Shoe Records
shoe1 = Shoe.objects.create(product=product1)
shoe2 = Shoe.objects.create(product=product2)
shoe3 = Shoe.objects.create(product=product3)
shoe4 = Shoe.objects.create(product=product4)

# Step 5: Create Style Records
style1 = Style.objects.create(color='Black', size=9, type='Running', material='Mesh')
style2 = Style.objects.create(color='White', size=8, type='Casual', material='Leather')
style3 = Style.objects.create(color='Red', size=10, type='Training', material='Synthetic')
style4 = Style.objects.create(color='Blue', size=7, type='Sports', material='Fabric')

# Step 6: Create ShoeStyle Records
ShoeStyle.objects.create(shoe=shoe1, style=style1)
ShoeStyle.objects.create(shoe=shoe2, style=style2)
ShoeStyle.objects.create(shoe=shoe3, style=style3)
ShoeStyle.objects.create(shoe=shoe4, style=style4)

# Step 7: Create More Products and Supporting Records
brands = [brand1, brand2, brand3, brand4]
hsn_codes = [hsn1, hsn2, hsn3]
styles = [
    {'color': 'Green', 'size': 8, 'type': 'Training', 'material': 'Synthetic'},
    {'color': 'Yellow', 'size': 9, 'type': 'Running', 'material': 'Mesh'},
    {'color': 'Brown', 'size': 7, 'type': 'Sports', 'material': 'Leather'},
    {'color': 'Gray', 'size': 10, 'type': 'Casual', 'material': 'Fabric'}
]

for i in range(5, 21):
    product = Product.objects.create(
        name=f'Product{i}',
        price_inclusive=3000 + i * 100,
        description=f'Description for product {i}',
        brand=brands[i % 4],
        gst_rate=hsn_codes[i % 3].GSTe,
        hsn_code=hsn_codes[i % 3].hsn_code
    )
    shoe = Shoe.objects.create(product=product)
    
    style_data = styles[i % 4]
    style = Style.objects.create(
        color=style_data['color'],
        size=style_data['size'],
        type=style_data['type'],
        material=style_data['material']
    )
    ShoeStyle.objects.create(shoe=shoe, style=style)

# Step 8: Verify Record Creation
Product.objects.all()  # to list all products
Shoe.objects.all()     # to list all shoes
Style.objects.all()    # to list all styles
ShoeStyle.objects.all() # to list all shoe styles




















from your_app.models import Brand, HsnCode, Product, Shoe, Style, ShoeStyle

# Step 1: Fetch existing Brands and HSN Codes
brands = list(Brand.objects.all())
hsn_codes = list(HsnCode.objects.all())

# Step 2: Create more styles to ensure variety
styles = [
    {'color': 'Orange', 'size': 8, 'type': 'Training', 'material': 'Synthetic'},
    {'color': 'Purple', 'size': 9, 'type': 'Running', 'material': 'Mesh'},
    {'color': 'Pink', 'size': 7, 'type': 'Sports', 'material': 'Leather'},
    {'color': 'Silver', 'size': 10, 'type': 'Casual', 'material': 'Fabric'},
    {'color': 'Gold', 'size': 6, 'type': 'Formal', 'material': 'Suede'}
]

# Step 3: Create 20 more Product records
for i in range(21, 41):
    # Create a new product
    product = Product.objects.create(name=f'Product{i}' , price_inclusive=3200 + i * 100 , description=f'Description for product {i}',brand=brands[i % len(brands)],gst_rate=hsn_codes[i % len(hsn_codes)].GSTe,hsn_code=hsn_codes[i % len(hsn_codes)].hsn_code)
    shoe = Shoe.objects.create(product=product)
    style_data = styles[i % len(styles)]
    style = Style.objects.create(color=style_data['color'],size=style_data['size'],type=style_data['type'],material=style_data['material'])
    # ShoeStyle.objects.create(shoe=shoe, style=style)

# Step 4: Verify the newly created products
Product.objects.all()  # to list all products
Shoe.objects.all()     # to list all shoes
Style.objects.all()    # to list all styles
ShoeStyle.objects.all() # to list all shoe styles
