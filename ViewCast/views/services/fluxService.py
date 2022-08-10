from typing import List
from datetime import datetime
from sqlalchemy import and_

from models.database.database import Session
from models.database.flux import Flux
from models.models.fluxModel import FluxModel, FluxShowModel
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

    def create_new_flux(self, flux_data, start_date, end_date, id_user):
        self.flux_repo.session = Session()
        self.flux_data_repo.session = Session()
        try:
            id_flux = int(datetime.now().timestamp() * 1000)
            new_flux: Flux = Flux(id=id_flux,
                                  url=id_flux,
                                  start_date=start_date if start_date != '' else None,
                                  end_date=end_date if end_date != '' else None,
                                  id_users=id_user)
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

    def get_flux_by_id_users(self, id_user) -> List[FluxShowModel]:
        self.flux_repo.session = Session()
        self.v_flux_repo.session = Session()
        result = []
        try:
            flux: list[Flux] = self.flux_repo.get_all_filter(Flux.id_users == id_user)
            for _flux in flux:
                flux_show_model: FluxShowModel = FluxShowModel.from_orm(_flux)
                data_cover: VFlux = self.v_flux_repo.get_first(and_(VFlux.url == flux_show_model.url,
                                                                    VFlux.position == 0))
                data_cover_model: VFluxModel = VFluxModel.from_orm(data_cover)
                flux_show_model.cover = data_cover_model.media
                result.append(flux_show_model)
        except Exception as ex:
            self.app.logger.error(f"Exception in get_flux_by_id_users(): {ex.args[0]}")
            result = []
            self.flux_repo.session.rollback()
            self.v_flux_repo.session.rollback()
        self.v_flux_repo.session.close()
        self.flux_repo.session.close()
        return result

    def check_available_flux(self, code):
        self.flux_repo.session = Session()
        result = False
        now = datetime.now()
        try:
            flux_model: FluxModel = FluxModel.from_orm(self.flux_repo.get_first(Flux.url == code))
            start_date = flux_model.start_date
            end_date = flux_model.end_date
            if start_date is not None and end_date is not None:
                result = (start_date < now < end_date)
            elif start_date is not None:
                result = start_date < now
            elif end_date is not None:
                result = end_date > now

        except Exception as ex:
            self.app.logger.error(f"Exception in check_available_flux(): {ex.args[0]}")
            result = False
            self.flux_repo.session.rollback()
        self.flux_repo.session.close()
        return result
