from unittest import mock
from unittest.mock import MagicMock

import pytest

from dao.director import DirectorDAO
from service.director import DirectorService


@pytest.fixture        # Подменяем обращение к базе
def director_dao():
    dao = DirectorDAO(None)
    dao.get_one = MagicMock()
    dao.get_all = MagicMock()
    dao.update = MagicMock()
    dao.delete = MagicMock()

    return dao


@pytest.fixture
def director_service(director_dao):
    return DirectorService(dao=director_dao)


@pytest.mark.parametrize(
    'data',
    (
        (
            {
                'id': 1,
                'name': 'test1',
            },
            {
                'id': 2,
                'name': 'test2',
            }
        )
    )
)
def test_get_one(director_service, data):
    director_service.dao.get_one.return_value = data

    assert director_service.get_one(1) == data       #{'id': 1, 'name': 'test',}


@pytest.mark.parametrize(
    'lenght, data',
    (
        (
            2,
            [
                {
                    'id': 1,
                    'name': 'test3',
                },
                {
                    'id': 2,
                    'name': 'test4',
                },
            ],
        ),
    ),
)
def test_get_all(director_service, lenght, data):
    director_service.dao.get_all.return_value = data

    test_result = director_service.get_all()
    assert isinstance(test_result, list)
    assert len(test_result) == lenght
    assert test_result == data


@pytest.mark.parametrize(
    'original_data, modified_data',
    (
        (
            {
                'id': 1,
                'name': 'test_original',
            },
            {
                'id': 1,
                'name': 'test_modified',
            },
        ),
    )
)
def test_partially_update(director_service, original_data, modified_data):
    director_service.dao.get_one.return_value = original_data
    director_service.partially_update(modified_data)
    director_service.dao.get_one.assert_called_once_with(original_data['id'])
    director_service.dao.update.assert_called_once_with(modified_data)


def test_delete(director_service):
    director_service.dao.delete(1)
    director_service.dao.delete.assert_called_once_with(1)


def test_update(director_service):
    director_service.update({})
    director_service.dao.update.assert_called_once_with({})

# @pytest.mark.parametrize(
#     'data',
#     (
#
#         {
#            'id': 1,
#            'name': mock.ANY,
#         },
#         {
#             'id': 2,
#             'name': mock.ANY,
#         }
#     ),
# )





