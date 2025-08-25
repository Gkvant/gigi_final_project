import pytest
from datetime import datetime
from gigi_final_project.pages.home_page import jwHomePage
from gigi_final_project.tests.conftest import setup_jw_org
from gigi_final_project.tests.data_file import FOOTER_TEXT, FOOTER_LINKS, footer_test_cases




class TestHomePage:

    @pytest.mark.parametrize("text, expected_url", footer_test_cases)
    def test_footer_links_match(self, setup_jw_org, text, expected_url):
        # Goal - check if link directs to desired page after click in footer
        home_page = jwHomePage(setup_jw_org)
        current_link = home_page.get_footer_link_with_(text)
        current_url = home_page.get_url_after_click(current_link)
        assert current_url == expected_url, f"After click footer link entitled {text} is directing to unexpected page"

    def test_copyright_year(self, setup_jw_org):
        # Goal - check if copyright year matches current year
        home_page = jwHomePage(setup_jw_org)
        current_year = str(datetime.now().year)
        jw_copyright_year = home_page.get_jw_copyright()
        assert jw_copyright_year == current_year, f"Copyright year that is on website {jw_copyright_year} does not match expected {current_year}"

    def test_footer_data_validation_text(self, setup_jw_org):
        # Goal - check if text on footer matches expected texts
        home_page = jwHomePage(setup_jw_org)
        footer_texts = home_page.get_footer_texts()
        assert footer_texts == FOOTER_TEXT, f"There is mismatch between expected footer text and actual footer text"

    def test_footer_data_validation_links(self, setup_jw_org):
        # Goal - check if links on footer matches expected links
        home_page = jwHomePage(setup_jw_org)
        footer_links = home_page.get_footer_links()
        assert footer_links == FOOTER_LINKS, f"There is mismatch between expected footer links and actual footer links"

    def test_footer_text_url_match(self, setup_jw_org):
        # Goal - check if links amount matches visible text amount in footer
        home_page = jwHomePage(setup_jw_org)
        footer_links = home_page.get_footer_links()
        footer_texts = home_page.get_footer_texts()
        count_text = len(footer_texts)
        count_link = len(footer_links)
        assert count_text == count_link, f"in footer expected to have {count_text} number of links, but actually presented are only {count_link}"
