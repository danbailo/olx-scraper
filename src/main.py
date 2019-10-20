from core import Olx
import utils

if __name__ == "__main__":

    args = utils.get_args()

    olx = Olx(args.link, args.sheet)
    olx.work()