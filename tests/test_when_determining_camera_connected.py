# coding: utf-8

from __future__ import unicode_literals

from pig.camera import camera_connected


def test_empty_message_should_yield_empty():
    seq = ['']
    expected = []

    assert expected == list(camera_connected(seq))


def test_remove_message_should_yield_false():
    seq = ['®remove Nikon D3000']
    expected = [False]

    assert expected == list(camera_connected(seq))


def test_add_message_should_yield_true():
    seq = ['®add Nikon D3000']
    expected = [True]

    assert expected == list(camera_connected(seq))


def test_add_remove_message_should_yield_true_false():
    seq = ['®add Nikon D3000', '®remove Nikon D3000']
    expected = [True, False]

    assert expected == list(camera_connected(seq))
