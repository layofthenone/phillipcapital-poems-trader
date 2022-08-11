from datetime import datetime


class RequestDataNaming:
    @staticmethod
    def future_contract_name_create(stock):
        exm = "F_EREGL0822 - (HISSE SENEDI-EREGL FUTURE)"
        currently_month = datetime.now().month + 1
        currently_year = datetime.now().year
        if len(str(currently_month)) == 1:
            currently_month = str(0) + str(currently_month)

        future_stock = "F_" + str(stock).upper() + \
                       str(currently_month) + \
                       (str(currently_year)[-2:]) + \
                       " - (HISSE SENEDI-" + str(stock).upper() + \
                       " FUTURE)"

        return future_stock


print(RequestDataNaming().future_contract_name_create("eregl"))
