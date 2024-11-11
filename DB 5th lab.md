---
marp: true
theme: uncover
style: |
  section {
    background-color: #0d1117;
    color: #c9d1d9;
  }
  h1 {
    color: #3fbf65;
  }
  h2, h3, h4, h5 {
    color: #58a6ff;
  }
---

# Desing Steps

---
- When a customer calls and places a delivery order, an employee records the order on a multiform order ticket.
- The employee captures such details as customer name, business or home address, phone number, order placement time, items ordered, and amount of sale.
---

![bg 100%](Images/Pasted%20image%2020241111174954.png)

---

![bg 80%](Images/Pasted%20image%2020241111180304.png)

---
- The multiform document is sent to the bouquet designer who will make the order ready for
delivery.
---

![bg 90%](Images/Pasted%20image%2020241111180431.png)
![bg 90%](Images/Pasted%20image%2020241111184003.png)

---


- Multiple copies of the shop’s order will be there (one for the client, the shop and one places in a reconciliation box)
- When the order is prepared, the delivery person delivers the order to the customer, removes one order ticket from the delivery box, collects payment for the order, and returns to Rachel’s Flowers shop (to take his second order if there are any).


---
- Upon arriving at Rachel’s Flowers and decor shop, the delivery person gives the order ticket and the payment to Rachel. 
- Each evening Rachel reconciles the order tickets stored in the reconciliation box with thedelivery payments and matching order tickets returned by the delivery person (to avoid any
discrepancies).
#### Do we have to model this?

---

##### Solution

You can have 
- ***delivering*** 
- ***payed***
statuses.

---

- Each evening Rachel reconciles the order tickets stored in the reconciliation box with the delivery payments and matching order tickets returned by the delivery person (to avoid any discrepancies).
#### Can our ER diagram do this?
---


- At the close of business ***each evening***, Rachel uses the data from the order tickets to update the goods sold and inventory files and generate the daily reports and to order new flowers from her flower supplier (different flower fields) if needed to maintain the stock levels.

---
#### Solution

1. You can find out from the **payed** orders which items have to updated.
2.
![](Images/Pasted%20image%2020241111185520.png)


---
##### We also have to check the stock levels so we have to differentiate what type of item we have!

---

![bg 20%](Images/Pasted%20image%2020241111192720.png)

---

- This online system must be able to monitor and report changes inventory material levels and ***to issue material orders and payments to suppliers***. Thus, the central data entity for this system will be an INVENTORY ITEM.

---
![bg 100%](Images/Pasted%20image%2020241111192605.png)

---

# Is this complete?

---

![bg 100%](Images/Pasted%20image%2020241111193021.png)

