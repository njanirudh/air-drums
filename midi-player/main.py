from drum_service import DrumService

if __name__ == "__main__" :

    drums_srv = DrumService()
    drums_srv.initialize_services()
    drums_srv.start()
