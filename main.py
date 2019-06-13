import argparse
import contact_manager


def main(args):
    cm  = contact_manager.ContactManager(args.file_path, args.driver_name)
    cm.run()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Personal Data loader')
    parser.add_argument('file_path', help='File with contact information')
    parser.add_argument('driver_name', help='File driver to be used, json_driver|xml_driver')
    args = parser.parse_args()
    main(args)