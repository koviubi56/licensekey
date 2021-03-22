"""
Licensekey is a very useful python module, if your software is not free.
You can (somehow) give the licensekey to the user, who paid for it, and at the start of the program, the user needs to write his/her license key.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.
"""
"""
    Copyright (C) 2021  Koviubi56

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""




import random
def generate(diff, pwd=1):
    """Generates a license key

    Args:
        diff (bool): The difficulty. False: Easy (2 elements)  True: Hard (6 elements with strings)
        pwd (int, optional): The password. Needs to be between 1 and 1000! Defaults to 1.

    Raises:
        OverflowError: If the password is greater than 1000.

    Returns:
        list: The license key.
    """
    if pwd > 1000:
        raise OverflowError("The password can't be 1001 or larger!!")
    if pwd == 1:
        print("[WARNING]")
        print("[!] If the password is 1, it can be easly finded!")
        print("[!] This is your own risk!")
        input("Press [ENTER] to continue. . .")
        print("/This is your own risk!/")
    if pwd in [10, 100, 1000]:
        print("[Info]")
        print("(i) If the password is 10; 100; or 1000, it's equal to 1, but just with (a) zero(s).")
        print("[!] This is your own risk!")
        input("Press [ENTER] to continue. . .")
    if diff:
        generated = [0, 0, 0, 0, 0, 0]
        generated[0] = random.randrange(100, 756) * pwd
        generated[1] = random.randrange(10, 69) * pwd
        generated[2] = random.choice(
            ["GAN", "DHI", "GNU", "AGP", "SZE", "RDA"])
        generated[3] = random.choice([252, 392, 483]) * pwd
        generated[4] = random.randrange(10000, 99999) * pwd
        generated[5] = 111
        while generated[5] in [000, 111, 222, 333, 444, 555, 666, 777, 888, 999]:
            generated[5] = random.randrange(100, 1000) * pwd
        return generated
    else:
        generated = [0, 222222222222]
        while generated[0] in [000, 111, 222, 333, 444, 555, 666, 777, 888, 999]:
            generated[0] = random.randrange(100, 999)
        generated[1] = random.randrange(1000000, 10000000) + pwd
        return generated


def isGood(diff, licensekey, pwd=1):
    """Checks if the key is an official license key.

    Args:
        diff (bool): Difficulty. False: Easy  True: Hard (be the same with the generating setting)
        licensekey (list): The licensekey.
        pwd (int, optional): The password. It needs to be between 1 and 1000. Defaults to 1. (be the same with the generating setting)

    Raises:
        OverflowError: If the password is greater than 1000.

    Returns:
        bool: Is the license key official?
    """
    if pwd > 1000:
        raise OverflowError("The password can't be 1001 or larger!")
    if diff:
        if licensekey[0] / pwd >= 100 and licensekey[0] / pwd < 756:
            if licensekey[1] / pwd >= 10 and licensekey[1] / pwd < 69:
                if licensekey[2] in ["GAN", "DHI", "GNU", "AGP", "SZE", "RDA"]:
                    if licensekey[3] / pwd in [252, 392, 483]:
                        if licensekey[4] / pwd >= 10000 and licensekey[4] / pwd < 99999:
                            if licensekey[5] / pwd in [000, 111, 222, 333, 444, 555, 666, 777, 888, 999]:
                                return False
                            else:
                                return True
        return False
    else:
        if licensekey[0] in [000, 111, 222, 333, 444, 555, 666, 777, 888, 999]:
            return False
        else:
            if 10000000 > licensekey[1] - pwd and licensekey[1] - pwd >= 1000000:
                return True
            else:
                return False


if __name__ == '__main__':
    print("To see the source code: https://github.com/koviubi56/licensekey")
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # ! This program is distributed in the hope that it will be useful, but                                          !
    # ! WITHOUT ANY WARRANTY without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE!
    # ! See the GNU Affero General Public License for more details.                                                 !
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    print("\nThis program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public License for more details.\n")
    while True:
        try:
            # ***************************************************************************
            # * Set "diff" (var) to True or False.                                      *
            # * If it's True, it's generating, and checking the "hard mode" licensekey, *
            # * If it's False, it's generating, and checking the "easy mode" licensekey.*
            # ***************************************************************************
            diff = True
            # !    ^               !
            # !    | True / False  !
            # **************************************************
            # * Set the password to a number between 1 and 1000*
            # **************************************************
            pwd = 1000
            # !   ^         !
            # !   | 1-1000  !
            if diff:
                print(str(generate(True, pwd)))
                u1 = int(input(">"))
                u2 = int(input(">"))
                u3 = input(">")
                u4 = int(input(">"))
                u5 = int(input(">"))
                u6 = int(input(">"))
                key = [u1, u2, u3, u4, u5, u6]
                print(str(isGood(True, key, pwd)))
            else:
                print(str(generate(False, pwd)))
                u1 = int(input(">"))
                u2 = int(input(">"))
                key = [u1, u2]
                print(str(isGood(False, key, pwd)))
        except:
            print("[ERROR]")
            print("Error code: RuntimeError")
            print("It's (99%) your problem! Please don't do that again!")
            input("Press [ENTER] to continue. . .")
        else:
            print("Generated and checked successfully!")
        finally:
            continue
