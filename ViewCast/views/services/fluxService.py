from typing import List
from datetime import datetime

from models.database.database import Session
from models.database.flux import Flux
from models.models.fluxModel import FluxModel
from models.repos.fluxRepo import FluxRepo
from models.database.fluxData import FluxData
from models.models.fluxDataModel import FluxDataModel
from models.repos.fluxDataRepo import FluxDataRepo
from models.database.v_flux import VFlux
from models.repos.v_fluxRepo import VFluxRepo
from models.models.v_fluxModel import VFluxModel

class FluxService:
    def __init__(self, app):
        _session = Session()
        self.app = app
        self.flux_repo = FluxRepo(_session, Flux)
        self.flux_data_repo = FluxDataRepo(_session, FluxData)
        self.v_flux_repo= VFluxRepo(_session, VFlux)

    def create_new_flux(self, flux_data):
        self.flux_repo.session = Session()
        self.flux_data_repo.session = Session()
        try:
            id_flux = int(datetime.now().timestamp() * 1000)
            new_flux: Flux = Flux(id=id_flux,
                                  url=id_flux)
            self.flux_repo.insert(new_flux)
            for elem in flux_data:
                new_flux_data: FluxData = FluxData(position=elem.get("position"),
                                                   time=elem.get("time"),
                                                   id_flux=id_flux,
                                                   id_media=elem.get("id_media"))
                self.flux_data_repo.insert(new_flux_data, False)

            self.flux_repo.commit()
            self.flux_data_repo.commit()
        except Exception as ex:
            self.app.logger.error(f"Exception in create_new_flux(): {ex.args[0]}")
            self.flux_data_repo.session.rollback()
            self.flux_repo.session.rollback()
        self.flux_repo.session.close()
        self.flux_data_repo.session.close()

    def get_flux_by_url(self, url):
        self.v_flux_repo.session = Session()
        result = []
        try:
            v_flux: list[VFlux] = self.v_flux_repo.get_all_filter(VFlux.url == url)
            for _v_flux in v_flux:
                v_flux_model: VFluxModel = VFluxModel.from_orm(_v_flux)
                result.append(v_flux_model)

        except Exception as ex:
            self.app.logger.error(f"Exception in get_flux_by_url(): {ex.args[0]}")
            result = []
            self.flux_repo.session.rollback()
        self.v_flux_repo.session.close()
        return result
