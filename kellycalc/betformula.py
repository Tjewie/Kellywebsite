import random
import matplotlib.pyplot as plt

def winprob(odds, edge):

    return 1 / (odds - edge)

def lossprob(odds, edge):

    return 1 - winprob(odds, edge)

def nettoodds(odds):

    return odds - 1

def kellycriterion(odds, edge):

    return (nettoodds(odds) * winprob(odds, edge) - lossprob(odds, edge)) / nettoodds(odds)

def betsize(odds, edge, bankroll):
    return kellycriterion(odds, edge) * bankroll

#----------------------------------------------------------------------------------------------------------------

def oddsgenerator():

    return round(random.uniform(1.05, 2.15), 2)

def odds_to_percentage(odds):

    return 1 / odds * 100

def win_or_loss_sim(odds, edge):

    if random.uniform(0, 100) <= odds_to_percentage(odds - edge):

        return True  # True is win

    else:
        return False


def bankroll_change(odds, edge, bankroll, tries):

    bankrolls = []

    for bet in range(0, tries):

        if win_or_loss_sim(odds, edge):

            bankroll += (betsize(odds, edge, bankroll) * nettoodds(odds))

            bankrolls.append(bankroll)

        else:

            bankroll -= betsize(odds, edge, bankroll)

            bankrolls.append(bankroll)

    return bankrolls


def net_win(bankrolls):

    return bankrolls[len(bankrolls) - 1] - bankrolls[0]

def total_revenue(history_list): # forkert! jeg lægger bankrolls sammen - det er ikke hvad jeg har staket hver gang. Jeg skal lægge betsizes sammen

    total_revenue = 0

    for n in history_list:

        total_revenue += n

    return total_revenue

#print(total_revenue(bankrolls))
#print(net_win(bankrolls))
#print(bankrolls[len(bankrolls) - 1])

def roi(bankrolls):

    return net_win(bankrolls) / total_revenue(bankrolls)

#print(roi(bankrolls))
#print(net_win(bankrolls))


if __name__ == '__main__':

    bankrolls = bankroll_change(1.5, 0.015, 50000, 1000)

    plt.plot(bankrolls)
    plt.show()