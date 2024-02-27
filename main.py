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
descrs = []
prices = []

IDX_SANDWICH_CHICKEN = 0
descrs.append('Chicken')
prices.append(5.25)

IDX_SANDWICH_BEEF = 1
descrs.append('Beef')
prices.append(6.25)

IDX_SANDWICH_TOFU = 2
descrs.append('Tofu')
prices.append(5.75)

IDX_BEVERAGE_SMALL = 3
descrs.append('Small')
prices.append(1.0)

IDX_BEVERAGE_MEDIUM = 4
descrs.append('Medium')
prices.append(1.5)

IDX_BEVERAGE_LARGE = 5
descrs.append('Large')
prices.append(2.0)

IDX_FRIES_SMALL = 6
descrs.append('Small')
prices.append(1.5)

IDX_FRIES_MEDIUM = 7
descrs.append('Medium')
prices.append(1.5)

IDX_FRIES_LARGE = 8
descrs.append('Large')
prices.append(2.0)


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
        prompt += f'{descrs[idx]}: ${prices[idx]:.2f}, '
    prompt = prompt.removesuffix(', ')
    prompt += " ?>"
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
    order[IDX_SANDWICH_TYPE] = descrs[idx]
    order[IDX_SANDWICH_COST] = prices[idx]

    order[IDX_TOTAL_COST] += prices[idx]


def get_beverage():
    yesno = input("Would you like a beverage?>")
    if yesno is None or len(yesno) == 0:
        return
    if yesno[:1].lower() != 'y':
        return

    # create prompt
    prompt = "Which beverage size you like to order: "
    for idx in range(IDX_BEVERAGE_SMALL, IDX_BEVERAGE_LARGE + 1):
        prompt += f'{descrs[idx]}: ${prices[idx]:.2f}, '
    prompt = prompt.removesuffix(', ')
    prompt += " >"
    choice = input(prompt)
    if choice is None or len(choice) == 0:
        choice = "unknown"
    choice = choice[:1].lower()
    idx = -1
    match choice[:1]:

        case 's':
            idx = IDX_BEVERAGE_SMALL
        case 'm':
            idx = IDX_BEVERAGE_MEDIUM
        case 'l':
            idx = IDX_BEVERAGE_LARGE

    if idx == -1:
        print('Invalid beverage size. No beverage will be ordered.')
        return

    order[IDX_BEVERAGE_SIZE] = descrs[idx]
    order[IDX_BEVERAGE_COST] = prices[idx]

    order[IDX_TOTAL_COST] += prices[idx]


def get_fries():
    yesno = input("Would you like fries?>")
    if yesno is None or len(yesno) == 0:
        return
    if yesno[:1].lower() != 'y':
        return

    # create prompt
    prompt = "Which fries size you like to order: "
    for idx in range(IDX_FRIES_SMALL, IDX_FRIES_LARGE + 1):
        prompt += f'{descrs[idx]}: ${prices[idx]:.2f}, '
    prompt = prompt.removesuffix(', ')
    prompt += " >"
    choice = input(prompt)
    if choice is None or len(choice) == 0:
        choice = "unknown"
    choice = choice[:1].lower()
    idx = -1
    match choice[:1]:

        case 's':
            idx = IDX_FRIES_SMALL
            yesno = input('Do you want to super-size to large size?>').strip().lower()
            if yesno[:1] == 'y':
                idx = IDX_FRIES_LARGE

        case 'm':
            idx = IDX_FRIES_MEDIUM
        case 'l':
            idx = IDX_FRIES_LARGE

    if idx == -1:
        print('Invalid fries size. No fries will be ordered.')
        return

    order[IDX_FRIES_SIZE] = descrs[idx]
    order[IDX_FRIES_COST] = prices[idx]

    order[IDX_TOTAL_COST] += prices[idx]


def check_for_discount():
    if order[IDX_SANDWICH_COST] > 0 and order[IDX_BEVERAGE_COST] > 0 and order [IDX_TOTAL_COST] > 0:
        order[IDX_DISCOUNT_APPLIED] = True
        order[IDX_TOTAL_COST] -= 1


def display_order():
    output = 'Your order:'

    # add sandwich information
    item_name = 'Sandwich:'
    output += f'\n\t{item_name:12}'
    if order[IDX_SANDWICH_TYPE] == 'None':
        output += 'none'
    else:
        output += f'{order[IDX_SANDWICH_TYPE]:10} ${order[IDX_SANDWICH_COST]:6.2f}'

    # add beverage information
    item_name = 'Beverage:'
    output += f'\n\t{item_name:12}'
    if order[IDX_BEVERAGE_SIZE] == 'None':
        output += 'none'
    else:
        output += f'{order[IDX_BEVERAGE_SIZE]:10} ${order[IDX_BEVERAGE_COST]:6.2f}'

    # add fries information
    item_name = 'Fries:'
    output += f'\n\t{item_name:12}'
    if order[IDX_FRIES_SIZE] == 'None':
        output += 'none'
    else:
        output += f'{order[IDX_FRIES_SIZE]:10} ${order[IDX_FRIES_COST]:6.2f}'

    # show discount if applied
    if order[IDX_DISCOUNT_APPLIED]:
        output += '\n\t** $1 discount was applied **'

    # total cost
    output += f'\nTotal: ${order[IDX_TOTAL_COST]}'

    print(output)


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


if __name__ == '__main__':
    print(f'Combo Menu using lists and python version {get_python_version()}')
    new_order()
    get_sandwich()
    get_beverage()
    get_fries()
    check_for_discount()
    display_order()
