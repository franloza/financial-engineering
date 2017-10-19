import math

# Simple interest functions
def simple_interest_fv(P, r, t):
    """The future value of a simple interest product consists of the initial deposit, called the
    principal and denoted by P, plus all the interest earned since the money was deposited in the account

    Parameters
    ----------
    P: float
        Principal, initial deposit.
    r: float
        Interest rate
    t: float
        Time, expressed in years.
    """
    return P*(1 + t*r)


def simple_interest_pv(V_t, r, t):
    """The present value of a simple interest product tries to find the initial sum whose value at time t is given.
    Also called discounted value.

    Parameters
    ----------
    V_t: float
        Future value at time t.
    r: float
        Interest rate
    t: float
        Time, expressed in years.
    """
    return V_t * (1/(1 + t * r))


def perpetuity_pv(C, r):
    """A perpetuity is a sequence of payments of a fixed amount to be made at equal time intervals and continuing
     indefinitely into the future.

     Parameters
    ----------
    C: float
       Payment at equal time intervals.
    r: float
        Interest rate
     """
    return C / r


# Compounded interest functions
def compounded_interest_fv(P, r, t, m):
    """ Compunded interest rate assumes that the interest earned will now be added to the principal periodically,
       for example, annually, semi-annually, quarterly, monthly or on a daily basis.
    Parameters
    ----------
    P: float
        Principal, initial deposit.
    r: float
        Interest rate
    t: float
        Time, expressed in years.
    m: float
        Compounding period. Amount of payments made per annum.

    """
    return P*(1 + r/m)**(t*m)


def compounded_interest_pv(V_t, r, t, m):
    """The present value of a compounded interest product tries to find the initial sum whose value at time t is given.
       Also called discounted value.

    Parameters
    ----------
    V_t: float
        Future value at time t.
    r: float
        Interest rate
    t: float
        Time, expressed in years.
    m: float
        Compounding period. Amount of payments made per annum.

    """
    return V_t*(1/(1 + r/m)**(t*m))


def annuity_pv(C, r, n):
    """An annuity is a sequence of finitely many payments of a fixed amount due  at equal time intervals. Assuming that
      annual compounding applies, we shall find the present value of such a stream of payments.

     Parameters
    ----------
    C: float
       Payment at equal time intervals.
    r: float
        Interest rate
    n: int
        Number of payments
     """
    return C * _annuity_pv_factor(r,n)


def annuity_payment(P, r, n):
    """Annuity payment given a principal, an amount of payments and an interest rate

     Parameters
    ----------
    P: float
       Principal, initial deposit.
    r: float
        Interest rate
    n: int
        Number of payments
    """
    return P/_annuity_pv_factor(r, n)


def _annuity_pv_factor(r,n):
    """Present value factor for an annuity. Formula equivalent to C/r + r + C/(1+r)**2 + ... + C/(1+r)**n
    Parameters
    ----------.
    r: float
        Interest rate
    n: int
        Number of payments
    """
    return (1 - (1/(1+r)**n)) / r


def continuous_compounding_fv(P, r, t):
    """Continuous compounding is a good approximation of the case of periodic compounding
    when the frequency m is large. It is simpler and lends itself more readily to
    transformations than the formula for periodic compounding.

    Parameters
    ----------
    P: float
        Principal, initial deposit.
    r: float
        Interest rate
    t: float
        Time, expressed in years.
    """

    return math.exp(t*r)*P


def continuous_compounding_pv(V_t, r, t):
    """Present Value of continuous compounding interest.

    V_t: float
        Future value at time t.
    r: float
        Interest rate
    t: float
        Time, expressed in years.
    """
    return V_t * math.exp(-t*r)


def effective_rate(r, m=1, method="continuous"):
    """The effective rate is the rate that gives the same growth factor over a one year period under annual
    compounding.

    Parameters
    ----------
    r: float
        Interest rate
    m: float, optional
        Compounding period. Amount of payments made per annum
    method: str, optional
        Compounding method. It can be "continuous" or "periodic"
    """
    if method == "continuous":
        return math.exp(r) - 1
    elif method == "periodic":
        return (1 + r/m)**m - 1
    else:
        return ValueError("The compounding method is not valid")