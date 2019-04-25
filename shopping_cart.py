class ShoppingCart():
    import numpy as np
    def __init__(self,total=0,employee_discount=None,items=[]):
        self.total=total
        self.employee_discount=employee_discount
        self.items=[]
    def add_item(self, item_name=None, item_price=None,item_quantity=1):
        for i in list(range(item_quantity)):
            self.items.append({"name": item_name,"price":item_price})
            self.total+=item_price
        return self.total
    def mean_item_price(self):
        return self.total/len(self.items)
    def median_item_price(self):
        holder=[]
        for i in self.items:
            holder.append(i['price'])
        if len(holder)%2==0:
            a=int(len(holder)/2)
            b=a-1
            return (holder[a]+holder[b])/2
        c=int(len(holder)/2)
        return holder[c]
    def apply_discount(self):
        if self.employee_discount:
            return self.total*(1-self.employee_discount/100)
        else: 'Sorry there is no discout applied to your cart'
    def void_last_item(self):
        if len(self.items)>0:
            returned_item=self.items.pop()
        else: 
            return 'There are no items in your cart'
        self.total-=returned_item['price']