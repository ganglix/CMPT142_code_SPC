# Given variables:
nation = "Canada !!!"
nation_motto = "From sea to Sea"

print(
    # Write expressions to:
    # (a) Determine if nation has only alphabetic letters and digits
    nation.isalnum(),

    # (b) Remove "!" characters and whitespace from nation
    nation.replace("!", "").replace(" ", ""),
    nation.replace("!", "").replace(" ", "").isalnum(),

    # (c) Find the location of the first "Sea" substring in nation_motto
    nation_motto.find("Sea"),

    # (bonus) find the location of "sea", not case sensitive
    nation_motto.upper().find("SEA")

    , sep="\n"
)
