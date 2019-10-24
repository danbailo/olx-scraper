from core import Olx
import args

if __name__ == "__main__":
    args = args.get_args_main()
    olx = Olx(args.link, args.sheet)
    olx.work()