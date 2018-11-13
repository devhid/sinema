from project.sinema import create_app

if __name__ == "__main__":
    app = create_app(config_file='settings/dev.py')
    app.run()

