from unittest import mock
from unittest.mock import MagicMock

import pytest

from dao.genre import GenreDAO
from service.genre import GenreService


@pytest.fixture        # Подменяем обращение к базе
def genre_dao():
    dao = GenreDAO(None)
    dao.get_one = MagicMock()
    dao.get_all = MagicMock()
    dao.update = MagicMock()
    dao.delete = MagicMock()

    return dao


@pytest.fixture
def genre_service(genre_dao):
    return GenreService(dao=genre_dao)


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
def test_get_one(genre_service, data):
    genre_service.dao.get_one.return_value = data

    assert genre_service.get_one(1) == data


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
def test_get_all(genre_service, lenght, data):
    genre_service.dao.get_all.return_value = data

    test_result = genre_service.get_all()
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
def test_partially_update(genre_service, original_data, modified_data):
    genre_service.dao.get_one.return_value = original_data
    genre_service.partially_update(modified_data)
    genre_service.dao.get_one.assert_called_once_with(original_data['id'])
    genre_service.dao.update.assert_called_once_with(modified_data)


def test_delete(genre_service):
    genre_service.dao.delete(1)
    genre_service.dao.delete.assert_called_once_with(1)


def test_update(genre_service):
    genre_service.update({})
    genre_service.dao.update.assert_called_once_with({})

