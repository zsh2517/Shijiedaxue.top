#run python
# 由于没有认真写，所以每次和每次的代码不一样。（差换行）
# 以及不是真正的递归，因为丽琪调用需要两句话。（当然如果被人改成了print("runpython")调用缓存除外。
import sys
f_name = sys.argv[0]
def main():
    with open(f_name, "r", encoding="utf-8") as f:
        content = f.read()
        content = content.split("#" + " QWQWQ")
        choice = sw()
        if choice == 2:
            print("#run python")
            print(content[0])
            print("#" + " QWQWQ")
            print("def sw():")
            print("    return 1")
            print("    # 1 SteveBot")
            print("    # 2 丽琪")
            print("main()")
        else:
            print("python")
            print(content[0])
            print("#" + " QWQWQ")
            print("def sw():")
            print("    return 2")
            print("    # 1 SteveBot")
            print("    # 2 丽琪")
            print("main()")
            print("endpython")
        print()
# QWQWQ
def sw():
    return 2
    # 1 SteveBot
    # 2 丽琪
main()