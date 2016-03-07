# -*- coding: utf-8 -*-
import os
import pytest


def test_resolver_check_candidate_ok_001(settings, parser, resolver):
    """resolver.ImportPathsResolver: Check candidates correct case 1"""
    candidates = resolver.candidate_paths("vendor")
    
    results = resolver.check_candidate_exists(settings.sample_path, candidates)
    
    assert results == os.path.join(settings.sample_path, "_vendor.scss")


def test_resolver_check_candidate_ok_002(settings, parser, resolver):
    """resolver.ImportPathsResolver: Check candidates correct case 2"""
    candidates = resolver.candidate_paths("components/_filename_test_2")
    
    results = resolver.check_candidate_exists(settings.sample_path, candidates)
    
    assert results == os.path.join(settings.sample_path, "components/_filename_test_2.scss")


def test_resolver_check_candidate_ok_003(settings, parser, resolver):
    """resolver.ImportPathsResolver: Check candidates correct case 3"""
    candidates = resolver.candidate_paths("components/filename_test_6.plop.scss")
    
    results = resolver.check_candidate_exists(settings.sample_path, candidates)
    
    assert results == os.path.join(settings.sample_path, "components/_filename_test_6.plop.scss")


def test_resolver_check_candidate_ok_004(settings, parser, resolver):
    """resolver.ImportPathsResolver: Check candidates correct case 4"""
    basepath = os.path.join(settings.sample_path, "components")
    candidates = resolver.candidate_paths("webfont")
    
    results = resolver.check_candidate_exists(basepath, candidates)
    
    assert results == os.path.join(basepath, "_webfont.scss")


def test_resolver_check_candidate_ok_005(settings, parser, resolver):
    """resolver.ImportPathsResolver: Check candidates correct case 5"""
    basepath = os.path.join(settings.sample_path, "components")
    candidates = resolver.candidate_paths("../components/webfont_icons")
    
    results = resolver.check_candidate_exists(basepath, candidates)
    
    assert results == os.path.join(basepath, "../components/_webfont_icons.scss")


def test_resolver_check_candidate_wrong_001(settings, parser, resolver):
    """resolver.ImportPathsResolver: Check candidates wrong case 1"""
    candidates = resolver.candidate_paths("dont_exists")
    
    results = resolver.check_candidate_exists(settings.sample_path, candidates)
    
    assert results == False


def test_resolver_check_candidate_wrong_002(settings, parser, resolver):
    """resolver.ImportPathsResolver: Check candidates wrong case 2"""
    candidates = resolver.candidate_paths("css_filetest.sass")
    
    results = resolver.check_candidate_exists(settings.sample_path, candidates)
    
    assert results == False