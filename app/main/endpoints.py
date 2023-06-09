from datetime import datetime
from flask import request, jsonify
from ..auth import token_required
from .. import app
from ..models import *
from . import main_bp


# to get all products
@main_bp.route("/getallproducts", methods=["GET"])
@token_required
def getAllProducts(current_user):
    response_object = {
        "status": "fail",
        "message": "error occured"
    }

    try:
        if request.method == "GET":
            products = Product.query.all()
            response_object["data"] = []

            for prd in products:
                response_object["data"].append({
                    "id": prd.id,
                    "name": prd.name,
                    "price": prd.price,
                    "description": prd.description,
                    "available_qty": prd.available_qty,
                    "ordered_qty": prd.ordered_qty,
                    "total_qty": prd.total_qty,
                    "promo": prd.promo,
                    "img_link": prd.img_link,
                    "category": Category.query.filter_by(id=prd.category_id).first().name,
                    "promo_price": int(prd.price-(prd.price * prd.promo / 100))
                })

            response_object["status"], response_object["message"] = "success", "-"
            return jsonify(response_object := response_object["data"])
            # return jsonify(response_object)
        
        return response_object
    except Exception as e:
         response_object["message"] = str(e)
         return jsonify(response_object)
    

# to get all available products
@main_bp.route("/getallavailableproducts", methods=["GET"])
@token_required
def getAllAvailableProducts(current_user):
    response_object = {
        "status": "fail",
        "message": "error occured"
    }

    try:
        if request.method == "GET":
            available_products = Product.query.filter(Product.available_qty > 0).all()
            response_object["data"] = []

            for aprd in available_products:
                response_object["data"].append({
                    "id": aprd.id,
                    "name": aprd.name,
                    "price": aprd.price,
                    "description": aprd.description,
                    "available_qty": aprd.available_qty,
                    "ordered_qty": aprd.ordered_qty,
                    "total_qty": aprd.total_qty,
                    "promo": aprd.promo,
                    "img_link": aprd.img_link,
                    "category": Category.query.filter_by(id=aprd.category_id).first().name,
                    "promo_price": int(aprd.price-(aprd.price * aprd.promo / 100))
                })

            response_object["status"], response_object["message"] = "success", "-"
            return jsonify(response_object := response_object["data"])
            # return jsonify(response_object)
        
        return response_object
    except Exception as e:
         response_object["message"] = str(e)
         return jsonify(response_object)


# to get all promo products
@main_bp.route("/getallpromos", methods=["GET"])
@token_required
def getAllPromos(current_user):
    response_object = {
        "status": "fail",
        "message": "error occured"
    }

    try:
        if request.method == "GET":
            promos = Product.query.filter((Product.promo > 0) & (Product.promo <= 100)).all()
            response_object["data"] = []

            for prd in promos:
                response_object["data"].append({
                    "id": prd.id,
                    "name": prd.name,
                    "price": prd.price,
                    "description": prd.description,
                    "available_qty": prd.available_qty,
                    "ordered_qty": prd.ordered_qty,
                    "total_qty": prd.total_qty,
                    "promo": prd.promo,
                    "img_link": prd.img_link,
                    "category": Category.query.filter_by(id=prd.category_id).first().name,
                    "promo_price": int(prd.price-(prd.price * prd.promo / 100))
                })

            response_object["status"], response_object["message"] = "success", "-"
            return jsonify(response_object := response_object["data"])
            # return jsonify(response_object)
        
        return response_object
    except Exception as e:
         response_object["message"] = str(e)
         return jsonify(response_object)
    

# to get all available products
@main_bp.route("/getallavailablepromos", methods=["GET"])
@token_required
def getAllAvailablePromos(current_user):
    response_object = {
        "status": "fail",
        "message": "error occured"
    }

    try:
        if request.method == "GET":
            available_promos = Product.query.filter((Product.available_qty > 0) & (Product.promo > 0) & (Product.promo <= 100)).all()
            response_object["data"] = []

            for aprd in available_promos:
                response_object["data"].append({
                    "id": aprd.id,
                    "name": aprd.name,
                    "price": aprd.price,
                    "description": aprd.description,
                    "available_qty": aprd.available_qty,
                    "ordered_qty": aprd.ordered_qty,
                    "total_qty": aprd.total_qty,
                    "promo": aprd.promo,
                    "img_link": aprd.img_link,
                    "category": Category.query.filter_by(id=aprd.category_id).first().name,
                    "promo_price": int(aprd.price-(aprd.price * aprd.promo / 100))
                })

            response_object["status"], response_object["message"] = "success", "-"
            return jsonify(response_object := response_object["data"])
            # return jsonify(response_object)
        
        return response_object
    except Exception as e:
         response_object["message"] = str(e)
         return jsonify(response_object)
    

# to get all sales detail carts
@main_bp.route("/getallcategories", methods=["GET"])
@token_required
def getAllCategories(current_user):
    response_object = {
        "status": "fail",
        "message": "error occured"
    }

    try:
        if request.method == "GET":
            # to get all detail carts
            theCategories = Category.query.all()
            response_object["data"] = [ctg.name for ctg in theCategories]

            response_object["status"], response_object["message"] = "success", "-"
            return jsonify(response_object := response_object["data"])
            # return jsonify(response_object)

        return response_object
    except Exception as e:
         response_object["message"] = str(e)
         return jsonify(response_object)


# to get all sales orders [CLEAR]
@main_bp.route("/getorders", methods=["GET"])
@token_required
def getOrders(current_user):
    response_object = {
        "status": "fail",
        "message": "error occured"
    }

    try:
        if request.method == "GET":
            orders = Order.query.filter_by(sales_id=current_user.username).all()
            response_object["data"] = []

            for ord in orders:
                response_object["data"].append({
                    "id": ord.id,
                    "image": Product.query.filter_by(id=DetailOrder.query.filter_by(order_id=ord.id).first().product_id).first().img_link,
                    "status": ord.status,
                    "total_price": ord.total_price,
                    "qty": ord.qty,
                    "customer": ord.customer_id,
                    "date": ord.date
                })

            response_object["status"], response_object["message"] = "success", "-"
            return jsonify(response_object := response_object["data"])
            # return jsonify(response_object)

        return response_object
    except Exception as e:
         response_object["message"] = str(e)
         return jsonify(response_object)
    

# to get detail order [CLEAR]
@main_bp.route("/getdetailorder/<order_id>", methods=["GET"])
@token_required
def getDetailOrder(current_user, order_id):
    response_object = {
        "status": "fail",
        "message": "error occured"
    }

    try:
        if request.method == "GET":
            theOrder = Order.query.filter_by(sales_id=current_user.username, id=order_id).first()
            print(theOrder)
            if theOrder:
                theDetailOrders = DetailOrder.query.filter_by(order_id=theOrder.id).all()
                response_object["data"] = {
                    "customer": theOrder.customer_id,
                    "total_price": theOrder.total_price,
                    "total_qty": theOrder.qty,
                    "date": theOrder.date,
                    "detail_product": []
                }

                for dord in theDetailOrders:
                    theProduct = Product.query.filter_by(id=dord.product_id).first()
                    response_object["data"]["detail_product"].append({
                        "id": dord.id,
                        "name": theProduct.name,
                        "image": theProduct.img_link,
                        "qty": dord.qty,
                        "price": dord.qty*theProduct.price
                    })

                response_object["status"], response_object["message"] = "success", "-"
                return jsonify(response_object := response_object["data"])
            else:
                response_object["message"] = "you don't have the order"
                return jsonify(response_object)

        return response_object
    except Exception as e:
         response_object["message"] = str(e)
         return jsonify(response_object)
    

# to get all sales customers [CLEAR]
@main_bp.route("/getcustomers", methods=["GET"])
@token_required
def getCustomers(current_user):
    response_object = {
        "status": "fail",
        "message": "error occured"
    }

    try:
        if request.method == "GET":
            customers = Customer.query.filter_by(sales_id=current_user.username).all()
            response_object["data"] = []

            for cus in customers:
                response_object["data"].append({
                    "address": cus.address,
                    "name": cus.username,
                    "img_link": cus.img_link,
                    "sales": Sales.query.filter_by(username=cus.sales_id).first().name
                })

            response_object["status"], response_object["message"] = "success", "-"
            return jsonify(response_object := response_object["data"])
            # return jsonify(response_object)

        return response_object
    except Exception as e:
         response_object["message"] = str(e)
         return jsonify(response_object)
    

# to get sales data [CLEAR]
@main_bp.route("/getsales", methods=["GET"])
@token_required
def getSales(current_user):
    response_object = {
        "status": "fail",
        "message": "error occured"
    }

    try:
        if request.method == "GET":
            response_object["data"] = {
                "username": current_user.username,
                "name": current_user.name,
                "email": current_user.email,
                "status": current_user.verified
            }

            response_object["status"], response_object["message"] = "success", "-"
            return jsonify(response_object := response_object["data"])
            # return jsonify(response_object)

        return response_object
    except Exception as e:
         response_object["message"] = str(e)
         return jsonify(response_object)
    

# to get all information for cart page [CLEAR]
@main_bp.route("/getdetailcarts", methods=["GET"])
@token_required
def getDetailCarts(current_user):
    response_object = {
        "status": "fail",
        "message": "error occured"
    }

    try:
        if request.method == "GET":
            theCart = Cart.query.filter_by(sales_id=current_user.username).first()
            # to check if the query results are available
            if (theCart != None):
                # to get all detail carts
                theDetailCarts = DetailCart.query.filter_by(cart_id=theCart.id).all()
                response_object["data"] = []

                for dc in theDetailCarts:
                    theProduct = Product.query.filter_by(id=dc.product_id).first()
                    response_object["data"].append({
                        "id": dc.id,
                        "qty": dc.qty,
                        "product_id": theProduct.id,
                        "is_available": dc.is_available,
                        "product_name": theProduct.name,
                        "product_description": theProduct.description,
                        "product_img": theProduct.img_link,
                        "product_price": theProduct.price,
                        "product_available_qty": theProduct.available_qty,
                        "product_category": Category.query.filter_by(id=theProduct.category_id).first().name,
                        "promo": theProduct.promo,
                        "promo_price": int(theProduct.price-(theProduct.price * theProduct.promo / 100))
                    })
                
                response_object["status"], response_object["message"] = "success", "-"
                return jsonify(response_object := response_object["data"])
                # return jsonify(response_object)
            else:
                response_object["message"] = "cart is missing"

        return response_object
    except Exception as e:
         response_object["message"] = str(e)
         return jsonify(response_object)
    

# to check if a username for sales has been used or not
@main_bp.route("/getchecksalesusername/<username>", methods=["GET"])
def getCheckSalesUsername(username):
    response_object = {
        "status": "fail",
        "message": "error occured"
    }

    try:
        if request.method == "GET":
            # to get all detail carts
            theSales = Sales.query.filter_by(username=username).first()
            if (theSales == None):
                response_object["status"], response_object["message"] = "success", "-"
            else:
                response_object["message"] = "username has been used already"

            return jsonify(response_object)
            # return jsonify(response_object)

        return response_object
    except Exception as e:
         response_object["message"] = str(e)
         return jsonify(response_object)
    

# to verify/unverify a sales
@main_bp.route("/salesverifyunverify", methods=["PATCH"])
def salesVerifyUnverify():
    response_object = {
        "status": "fail",
        "message": "error occured"
    }

    try:
        if request.method == "PATCH":
            data = request.get_json()
            sales_username = data.get("sales_username")
            co_password = data.get("CO_PASSWORD")
            order = data.get("order")

            # defining
            theSales = Sales.query.filter_by(username=sales_username).first()

            # to check if the query results are available
            if (theSales != None):     
                if (co_password == app.config["CO_PASSWORD"]):
                    if (theSales.verified):
                        if (order == "verify"):
                            response_object["message"] = "the sales is verified already"
                        elif (order == "unverify"):
                            theSales.verified = False
                            db.session.commit()
                            response_object["status"], response_object["message"] = "success", "-"
                            return jsonify(response_object)
                        else:
                            response_object["message"] = "invalid order"
                    else:
                        if (order == "verify"):
                            theSales.verified = True
                            db.session.commit()
                            response_object["status"], response_object["message"] = "success", "-"
                            return jsonify(response_object)
                        elif (order == "unverify"):
                            response_object["message"] = "the sales is unverified already"
                        else:
                            response_object["message"] = "invalid order"
                else:
                    response_object["message"] = "you are not authorized to make this call" 
            else:
                response_object["message"] = "sales is missing"
                
        return jsonify(response_object)
    except Exception as e:
         response_object["message"] = str(e)
         return jsonify(response_object)


# to unsubscribe a customer to a sales
@main_bp.route("/unsubscribe", methods=["PATCH"])
@token_required
def unsubscribe(current_user):
    response_object = {
        "status": "fail",
        "message": "error occured"
    }

    try:
        if request.method == "PATCH":
            data = request.get_json()
            customer_username = data.get("customer_username")

            # defining
            theCustomer = Customer.query.filter_by(username=customer_username).first()

            # to check if the query results are available
            if (theCustomer != None):
                # to check whether or not the customer is already unsubscribed the Sales
                if (theCustomer in current_user.customers):        
                    current_user.customers.remove(theCustomer)
                    db.session.delete(theCustomer)
                    db.session.commit()
                    response_object["status"], response_object["message"] = "success", "-"
                    return jsonify(response_object)
                else:
                    response_object["message"] = "the customer is already unsubscribed the sales"
            else:
                response_object["message"] = "the customer is missing"

        return jsonify(response_object)
    except Exception as e:
         response_object["message"] = str(e)
         return jsonify(response_object)
    

# to confirm an order
@main_bp.route("/confirmorder", methods=["PATCH"])
def confirmOrder():
    response_object = {
        "status": "fail",
        "message": "error occured"
    }

    try:
        if request.method == "PATCH":
            data = request.get_json()
            order_id = data.get("order_id")
            sales_id = data.get("sales_username")

            # defining
            theOrder = Order.query.filter_by(id=order_id, sales_id=sales_id).first()

            # to check if the query result is available
            if theOrder != None:
                # to check whether or not the order is active
                if (theOrder.status == "active"):        
                    theOrder.status = "sent"        # update order status

                    db.session.commit()
                    response_object["status"], response_object["message"] = "success", "-"
                    return jsonify(response_object)
                else:
                    response_object["message"] = f"the order is already {theOrder.status}"
            else:
                response_object["message"] = "the order is missing"

        return jsonify(response_object)
    except Exception as e:
         response_object["message"] = str(e)
         return jsonify(response_object)
    

# to confirm an order
@main_bp.route("/cancelorder", methods=["PATCH"])
def cancelOrder():
    response_object = {
        "status": "fail",
        "message": "error occured"
    }

    try:
        if request.method == "PATCH":
            data = request.get_json()
            sales_id = data.get("sales_username")
            order_id = data.get("order_id")

            # defining
            theOrder = Order.query.filter_by(id=order_id, sales_id=sales_id).first()

            # to check if the query result is available
            if theOrder != None:
                # to check whether or not the order is active
                if (theOrder.status == "active"):        
                    # update product stock
                    for product in theOrder.products:
                        product.available_qty += DetailOrder.query.filter_by(order_id=order_id, product_id=product.id).first().qty

                    # update order status
                    theOrder.status = "canceled"        

                    db.session.commit()
                    response_object["status"], response_object["message"] = "success", "-"
                    return jsonify(response_object)
                else:
                    response_object["message"] = f"the order is already {theOrder.status}"
            else:
                response_object["message"] = "the order is missing"

        return jsonify(response_object)
    except Exception as e:
         response_object["message"] = str(e)
         return jsonify(response_object)
    

# to confirm an order [CLEAR]
@main_bp.route("/updatedetailcarts", methods=["PATCH"])
@token_required
def updateDetailCarts(current_user):
    response_object = {
        "status": "fail",
        "message": "error occured"
    }

    try:
        if request.method == "PATCH":
            data = request.get_json()
            updated_detail_carts = data.get("updated_detail_carts")

            # update the updated detail carts
            for newdc in updated_detail_carts:
                theDetailCart = DetailCart.query.filter_by(id=newdc["id"]).first()
                
                if (theDetailCart == None):
                    raise Exception("some of detail cart ids are invalid")
                
                theProduct = Product.query.filter_by(id=theDetailCart.product_id).first()

                theDetailCart.qty = newdc["qty"] if (theProduct.available_qty >= newdc["qty"]) else theProduct.available_qty     

            db.session.commit()
            response_object["status"], response_object["message"] = "success", "-"
            return jsonify(response_object)

        return jsonify(response_object)
    except Exception as e:
         response_object["message"] = str(e)
         return jsonify(response_object)
    

# to add new customer
@main_bp.route("/addnewcustomer", methods=["POST"])
@token_required
def addNewCustomer(current_user):
    response_object = {
        "status": "fail",
        "message": "error occured"
    }

    try:
        if request.method == "POST":
            data = request.get_json()
            customer_username = data.get("customer_username")
            customer_address = data.get("customer_address")
            customer_img_link = data.get("customer_img_link")

            # defining
            theCustomer = Customer.query.filter_by(username=customer_username).first()

            # to check if the query results are available
            if (theCustomer == None):
                newCustomer = Customer(username=customer_username, address=customer_address, img_link=customer_img_link, sales_id=current_user.username)
                db.session.add(newCustomer)
                db.session.commit()
                response_object["status"], response_object["message"] = "success", "-"
                return jsonify(response_object)
            else:
                response_object["message"] = "customer is already registered"

        return jsonify(response_object)
    except Exception as e:
         response_object["message"] = str(e)
         return jsonify(response_object)


# to add an order
@main_bp.route("/addorder", methods=["POST"])
@token_required
def addOrder(current_user):
    response_object = {
        "status": "fail",
        "message": "error occured"
    }

    try:
        if request.method == "POST":
            data = request.get_json()
            customer_username = data.get("customer_username")
            cartproductids = data.get("cartproductids")

            # defining
            theCustomer = Customer.query.filter_by(username=customer_username).first()
            theCart = Cart.query.filter_by(sales_id=current_user.username).first()
            theCartProducts = [
                DetailCart.query.filter_by(
                    id=cartproductid, cart_id=theCart.id
                ).first() for cartproductid in cartproductids
            ]

            # to check if the query results are available
            if (theCustomer != None) & (None not in theCartProducts):
                # to check if the customer inputted is already subscribed the sales
                if (theCustomer in current_user.customers):
                    # create an order
                    curdate = str(datetime.now().strftime(f"%d-%m-%Y"))
                    anOrder = Order(date=curdate, status="active", sales_id=current_user.username, customer_id=theCustomer.username, total_price=0)
                    db.session.add(anOrder)
                    db.session.commit()

                    newTotalPrice = 0

                    # create the detail
                    for cartProduct in theCartProducts:
                        theProduct = Product.query.filter_by(id=cartProduct.product_id).first()
                        theDetailOrder = DetailOrder(qty=cartProduct.qty, order_id=anOrder.id, product_id=theProduct.id)
                        db.session.add(theDetailOrder)

                        # update product stock
                        theProduct.available_qty -= cartProduct.qty if (cartProduct.qty <= theProduct.available_qty) else theProduct.available_qty

                        # remove the cart product
                        db.session.delete(cartProduct)

                        # update total price
                        if (theProduct.promo > 0):
                            newTotalPrice += int(theProduct.price - (theProduct.price * theProduct.promo / 100))*cartProduct.qty
                        else:
                            newTotalPrice += (theProduct.price*cartProduct.qty)

                    # update the total price in order
                    anOrder.total_price = newTotalPrice

                    db.session.commit()
                    response_object["status"], response_object["message"] = "success", "-"
                    return jsonify(response_object)
                else:
                    response_object["message"] = "the customer is not subscribed the sales yet"
            else:
                response_object["message"] = "either customer or list of cartproducts is missing"

        return jsonify(response_object)
    except Exception as e:
         response_object["message"] = str(e)
         return jsonify(response_object)
    

# to add certain number of product to the cart 
@main_bp.route("/addcartproduct", methods=["POST"])
@token_required
def addCartProduct(current_user):
    response_object = {
        "status": "fail",
        "message": "error occured"
    }

    try:
        if request.method == "POST":
            data = request.get_json()
            product_id = data.get("product_id")
            qty = data.get("qty")

            # defining
            theCart = Cart.query.filter_by(sales_id=current_user.username).first()
            theProduct = Product.query.filter_by(id=product_id).first()

            # to check if the query results are available
            if (theCart != None) & (theProduct != None):
                # to check if the product is already in the cart
                if (theDetailCart := DetailCart.query.filter_by(cart_id=theCart.id, product_id=theProduct.id).first()) != None:
                    theDetailCart.qty += qty if (theProduct.available_qty-theDetailCart.qty) >= qty else theProduct.available_qty-theDetailCart.qty
                else:
                    # to make sure if the product stock is 0, then it can not be added to the cart
                    if (theProduct.available_qty > 0):
                        # add the product to the cart
                        theDetailCart = DetailCart(qty=qty if theProduct.available_qty >= qty else theProduct.available_qty, is_available=True, cart_id=theCart.id, product_id=theProduct.id)
                        db.session.add(theDetailCart)
                    else:
                        response_object["message"] = "the product stock is not available"
                        return jsonify(response_object)
                        
                db.session.commit()
                response_object["status"], response_object["message"] = "success", "-"
                return jsonify(response_object)
            else:
                response_object["message"] = "either cart or product is missing"

        return jsonify(response_object)
    except Exception as e:
         response_object["message"] = str(e)
         return jsonify(response_object)
    

# to reduce certain number of product from the cart 
@main_bp.route("/reducecartproduct", methods=["POST"])
@token_required
def reduceCartProduct(current_user):
    response_object = {
        "status": "fail",
        "message": "error occured"
    }

    try:
        if request.method == "POST":
            data = request.get_json()
            product_id = data.get("product_id")
            qty = data.get("qty")

            # defining
            theCart = Cart.query.filter_by(sales_id=current_user.username).first()
            theProduct = Product.query.filter_by(id=product_id).first()

            # to check if the query results are available
            if (theCart != None) & (theProduct != None):
                # to check if the product is already in the cart
                if (theDetailCart := DetailCart.query.filter_by(cart_id=theCart.id, product_id=theProduct.id).first()) != None:
                    if theDetailCart.qty > qty:
                        theDetailCart.qty -= qty if theDetailCart.qty >= qty else theDetailCart.qty
                    else:
                        db.session.delete(theDetailCart)
                    
                    db.session.commit()
                    response_object["status"], response_object["message"] = "success", "-"
                else:
                    response_object["message"] = "the product has already been removed from the cart"
                        
                return jsonify(response_object)
            else:
                response_object["message"] = "either cart or product is missing"

        return jsonify(response_object)
    except Exception as e:
         response_object["message"] = str(e)
         return jsonify(response_object)
    

# to remove certain product from the cart 
@main_bp.route("/removecartproduct", methods=["POST"])
@token_required
def removeCartProduct(current_user):
    response_object = {
        "status": "fail",
        "message": "error occured"
    }

    try:
        if request.method == "POST":
            data = request.get_json()
            product_id = data.get("product_id")

            # defining
            theCart = Cart.query.filter_by(sales_id=current_user.username).first()
            theProduct = Product.query.filter_by(id=product_id).first()

            # to check if the query results are available
            if (theCart != None) & (theProduct != None):
                # to check if the product is already in the cart
                if (theDetailCart := DetailCart.query.filter_by(cart_id=theCart.id, product_id=theProduct.id).first()) != None:
                    # remove the product from the cart
                    db.session.delete(theDetailCart)

                    db.session.commit()
                    response_object["status"], response_object["message"] = "success", "-"
                else:
                    response_object["message"] = "product is not in the cart"
                        
                return jsonify(response_object)
            else:
                response_object["message"] = "either cart or product is missing"

        return jsonify(response_object)
    except Exception as e:
         response_object["message"] = str(e)
         return jsonify(response_object)
    

# to remove all detail carts 
@main_bp.route("/removeallcartproduct", methods=["POST"])
@token_required
def removeAllCartProduct(current_user):
    response_object = {
        "status": "fail",
        "message": "error occured"
    }

    try:
        if request.method == "POST":
            # defining
            theCart = Cart.query.filter_by(sales_id=current_user.username).first()

            # to check if the query results are available
            if (theCart != None):
                theDetailCarts = DetailCart.query.filter_by(cart_id=theCart.id).all()
                
                if (theDetailCarts == []):
                    response_object["message"] = "the cart is already empty"                        
                    return jsonify(response_object)
                
                for dc in theDetailCarts:
                    db.session.delete(dc)

                db.session.commit()
                response_object["status"], response_object["message"] = "success", "-"                        
                return jsonify(response_object)
            else:
                response_object["message"] = "either cart or product is missing"

        return jsonify(response_object)
    except Exception as e:
         response_object["message"] = str(e)
         return jsonify(response_object)

