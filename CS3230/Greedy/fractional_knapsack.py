def fractional_knapsack(Wi, Pi, max_weight):
    # Reconstruct the given Wi and Pi
    price_and_weight = []
    for i in range(len(Wi)):
        new_dict = {}
        new_dict["id"] = i
        new_dict["Wi"] = Wi[i]
        new_dict["Pi"] = Pi[i]
        new_dict["price_per_weight"] = new_dict["Pi"] / new_dict["Wi"] # Compute the price_per_weight
        price_and_weight.append(new_dict)
        
    # print(price_and_weight)
    # Sort in Descending order the price to weight 
    sorted_list = sorted(price_and_weight, key=lambda x: x["price_per_weight"], reverse=True)
    
    # print(sorted_list)
    curr_weight = 0
    final_knapsack = []
    # Iterate and keep count of max weight
    for item in sorted_list:
        if curr_weight >= max_weight:
            break
        # Only for 0/1 Knapsack
        # if (curr_weight + item["Wi"]) > max_weight:
        #     continue
        
        # If it can take the whole weight of the item
        if (curr_weight + item["Wi"]) <= max_weight:
            item["weight_chosen"] = 1.0 # 1/1 of the item
            final_knapsack.append(item)
            curr_weight += item["Wi"]
        else:
            remaining_weight = float(max_weight - curr_weight) / float(item["Wi"])
            item["weight_chosen"] = remaining_weight
            final_knapsack.append(item)
            curr_weight += (max_weight - curr_weight)
            
    return final_knapsack

# Wi = [3, 3, 2, 5, 1]
# Pi = [10, 15, 10, 20, 8]
# max_weight = 10

Wi = [1, 3, 5, 4]
Pi = [100, 30, 100, 20]
max_weight = 4

final_knapsack = fractional_knapsack(Wi, Pi, max_weight)
print("\nFinal Knapsack: ", final_knapsack)
final_weight = 0
for item in final_knapsack:
    final_weight += float(item["Pi"]) * float(item["weight_chosen"])

print(f"\nFinal Weight: {final_weight}")