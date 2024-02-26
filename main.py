import sys

# define order as a list
order = []

# define and populate portions of the order based on ordinal position
IDX_TOTAL_COST = 0
order.append(0)

IDX_SANDWICH_TYPE = 1
order.append("None")

IDX_SANDWICH_COST = 2
order.append(0)

IDX_BEVERAGE_SIZE = 3
order.append("None")

IDX_BEVERAGE_COST = 4
order.append(0)

IDX_FRIES_SIZE = 5
order.append("None")

IDX_FRIES_COST = 6
order.append(0)

IDX_DISCOUNT_APPLIED = 7
order.append(False)

# NOTE: indexes for descriptions and prices must be kept in sync with each other
descriptions = []
prices = []

IDX_SANDWICH_CHICKEN = 0
descriptions.append('Chicken')
prices.append(5.25)

IDX_SANDWICH_BEEF = 1
descriptions.append('Beef')
prices.append(6.25)

IDX_SANDWICH_TOFU = 2
descriptions.append('Tofu')
prices.append(5.75)


def new_order():
    order[IDX_TOTAL_COST] = 0

    order[IDX_SANDWICH_TYPE] = "None"
    order[IDX_SANDWICH_COST] = 0

    order[IDX_BEVERAGE_SIZE] = "None"
    order[IDX_BEVERAGE_COST] = 0

    order[IDX_FRIES_SIZE] = "None"
    order[IDX_FRIES_COST] = 0

    order[IDX_DISCOUNT_APPLIED] = False


def get_sandwich():
    # create prompt
    prompt = "Which sandwich would you like to order: "
    for idx in range(IDX_SANDWICH_CHICKEN, IDX_SANDWICH_TOFU + 1):
        prompt += f'{descriptions[idx]}: ${prices[idx]}, '
    prompt = prompt.removesuffix(', ')
    prompt += " >"
    choice = input(prompt)
    if choice is None or len(choice) == 0:
        choice = "unknown"
    choice = choice[:1].lower()
    idx = -1
    match choice[:1]:

        case 'c':
            idx = IDX_SANDWICH_CHICKEN
        case 'b':
            idx = IDX_SANDWICH_BEEF
        case 't':
            idx = IDX_SANDWICH_TOFU

    if idx == -1:
        print('Invalid sandwich choice. No sandwich will be ordered.')
        return
    order[IDX_SANDWICH_TYPE] = descriptions[idx]
    order[IDX_SANDWICH_COST] = prices[idx]

    order[IDX_TOTAL_COST] += prices[idx]

def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'

if __name__ == '__main__':
    print(f'Python version {get_python_version()}')
    new_order()
    get_sandwich()
    print(order)



