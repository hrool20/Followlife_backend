from flask_jwt_extended.view_decorators import jwt_required
from flask_restful import Resource, reqparse
from models.BaseClasses import BaseResponse
from models.Doctor import DoctorModel
from models.DoctorSpeciality import DoctorSpecialityModel


class DoctorSpeciality(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('id',
                        type=int,
                        required=False,
                        help='This field cannot be left blank.')
    parser.add_argument('medicalSpecialityId',
                        type=int,
                        required=True,
                        help='This field cannot be left blank.')

    @jwt_required
    def get(self, doctor_id=None, _id=None):
        if DoctorModel.find_by_id(doctor_id) is None:
            return BaseResponse.bad_request_response('Doctor does not exists.', {})

        if _id:
            doctor_speciality = DoctorSpecialityModel.find_by_id(_id)
            if doctor_speciality:
                return BaseResponse.ok_response('Successful.', doctor_speciality.json(only_spec=False))
            return BaseResponse.bad_request_response('Doctor speciality does not exists.', {})
        else:
            doctor = DoctorModel.find_by_id(doctor_id)
            doctor_specialities = list(map(lambda x: x.json(only_spec=True), doctor.doctorSpecialities))

            return BaseResponse.ok_response('Successful.', doctor_specialities)

    @jwt_required
    def post(self, doctor_id=None):
        try:
            data = DoctorSpeciality.parser.parse_args()

            if DoctorModel.find_by_id(doctor_id) is None:
                return BaseResponse.bad_request_response('Doctor does not exists.', {})
            elif DoctorSpecialityModel.verify_doctor_speciality(doctor_id, data['medicalSpecialityId']):
                return BaseResponse.bad_request_response('This doctor already have this specialities.', {})

            doctor_speciality = DoctorSpecialityModel(doctor_id=doctor_id, medical_speciality_id=data['medicalSpecialityId'])

            doctor_speciality.save_to_db()

            return BaseResponse.created_response('Doctor speciality created successfully.',
                                                 doctor_speciality.json(only_spec=False))
        except Exception as e:
            return BaseResponse.server_error_response(unicode(e))

    @jwt_required
    def put(self, doctor_id=None, _id=None):
        try:
            data = DoctorSpeciality.parser.parse_args()

            if DoctorModel.find_by_id(doctor_id) is None:
                return BaseResponse.bad_request_response('Doctor does not exists.', {})

            doctor_speciality = DoctorSpecialityModel.find_by_id(_id)
            if doctor_speciality:
                doctor_speciality.doctorId = data['doctorId'] if (data['doctorId'] is not None) \
                    else doctor_speciality.doctorId
                doctor_speciality.medicalSpecialityId = data['medicalSpecialityId'] \
                    if (data['medicalSpecialityId'] is not None) else doctor_speciality.medicalSpecialityId

                doctor_speciality.save_to_db()

                return BaseResponse.created_response('Doctor speciality updated successfully.',
                                                     doctor_speciality.json(only_spec=False))
            else:
                return BaseResponse.not_acceptable_response('Doctor speciality does not exists.', {})
        except Exception as e:
            return BaseResponse.server_error_response(unicode(e))

    @jwt_required
    def delete(self, doctor_id=None, _id=None):
        try:
            if DoctorModel.find_by_id(doctor_id) is None:
                return BaseResponse.bad_request_response('Doctor does not exists.', {})

            doctor_speciality = DoctorSpecialityModel.find_by_id(_id)
            if doctor_speciality:
                doctor_speciality.delete_from_db()

                return BaseResponse.ok_response('Doctor speciality deleted successfully.', {})
            else:
                return BaseResponse.not_acceptable_response('Doctor speciality does not exists.', {})
        except Exception as e:
            return BaseResponse.server_error_response(unicode(e))
