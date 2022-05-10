from unittest import mock
from unittest.mock import MagicMock

import pytest

from dao.movie import MovieDAO
from service.movie import MovieService


@pytest.fixture        # Подменяем обращение к базе
def movie_dao():
    dao = MovieDAO(None)
    dao.get_one = MagicMock()
    dao.get_all = MagicMock()
    dao.update = MagicMock()
    dao.delete = MagicMock()

    return dao


@pytest.fixture
def movie_service(movie_dao):
    return MovieService(dao=movie_dao)


@pytest.mark.parametrize(
    'data',
    (
        (
            {
                'id': 1,
                'title': 'test1',
                'description': 'test2',
                'trailer': 'test3',
                'year': 2015
            },

        )
    )
)
def test_get_one(movie_service, data):
    movie_service.dao.get_one.return_value = data

    assert movie_service.get_one(1) == data


@pytest.mark.parametrize(
    'lenght, data',
    (
        (
            1,
            [
                {
                    'id': 1,
                    'title': 'test1',
                    'description': 'test2',
                    'trailer': 'test3',
                    'year': 2015,
                },
            ],
        ),
    ),
)
def test_get_all(movie_service, lenght, data):
    movie_service.dao.get_all.return_value = data

    test_result = movie_service.get_all()
    assert isinstance(test_result, list)
    assert len(test_result) == lenght
    assert test_result == data


@pytest.mark.parametrize(
    'original_data, modified_data',
    (
        (
            {
                'id': 1,
                'title': 'test_original',
            },
            {
                'id': 1,
                'title': 'test_modified',
            },
        ),
    )
)
def test_partially_update(movie_service, original_data, modified_data):
    movie_service.dao.get_one.return_value = original_data
    movie_service.partially_update(modified_data)
    movie_service.dao.get_one.assert_called_once_with(original_data['id'])
    movie_service.dao.update.assert_called_once_with(modified_data)


def test_delete(movie_service):
    movie_service.dao.delete(1)
    movie_service.dao.delete.assert_called_once_with(1)


def test_update(movie_service):
    movie_service.update({})
    movie_service.dao.update.assert_called_once_with({})

