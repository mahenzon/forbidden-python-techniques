# from user_profile import (
#     getprofile,
#     setprofile,
# )
from sys import getsizeof
# import user_profile
import user_profile as up


def main():
    user = {"user_id": 1}
    profile = up.getprofile(user)
    print("got profile", profile)
    up.setprofile(user, profile)
    print(getsizeof(user))


if __name__ == "__main__":
    main()
