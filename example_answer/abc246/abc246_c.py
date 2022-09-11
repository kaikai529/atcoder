import sys
input = sys.stdin.readline

item_num, coupon, discount = map(int, input().split())
items_price = list(map(int, input().split()))

rest_coupon = coupon
for item_idx in range(item_num):
    use_coupon = min(rest_coupon, items_price[item_idx]//discount)
    items_price[item_idx] -= discount*use_coupon
    rest_coupon -= use_coupon
    if rest_coupon == 0:
        break

if rest_coupon == 0:
    print(sum(items_price))
else:
    items_price.sort(reverse=True)
    print(sum(items_price[rest_coupon:]))
