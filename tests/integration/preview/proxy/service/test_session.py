# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class SessionTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.preview.proxy.services(sid="KSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .sessions(sid="KCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://preview.twilio.com/Proxy/Services/KSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Sessions/KCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "service_sid": "KSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "status": "in-progess",
                "unique_name": "unique_name",
                "start_time": "2015-07-30T20:00:00Z",
                "links": {
                    "interactions": "https://preview.twilio.com/Proxy/Services/KSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Sessions/KCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Interactions",
                    "participants": "https://preview.twilio.com/Proxy/Services/KSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Sessions/KCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants"
                },
                "ttl": 100,
                "date_updated": "2015-07-30T20:00:00Z",
                "date_created": "2015-07-30T20:00:00Z",
                "end_time": "2015-07-30T20:00:00Z",
                "url": "https://preview.twilio.com/Proxy/Services/KSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Sessions/KCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "sid": "KCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.preview.proxy.services(sid="KSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                          .sessions(sid="KCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.preview.proxy.services(sid="KSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .sessions.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://preview.twilio.com/Proxy/Services/KSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Sessions',
        ))

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sessions": [],
                "meta": {
                    "previous_page_url": null,
                    "next_page_url": null,
                    "url": "https://preview.twilio.com/Proxy/Services/KSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Sessions?PageSize=50&Page=0",
                    "page": 0,
                    "first_page_url": "https://preview.twilio.com/Proxy/Services/KSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Sessions?PageSize=50&Page=0",
                    "page_size": 50,
                    "key": "sessions"
                }
            }
            '''
        ))

        actual = self.client.preview.proxy.services(sid="KSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                          .sessions.list()

        self.assertIsNotNone(actual)

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.preview.proxy.services(sid="KSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .sessions.create()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://preview.twilio.com/Proxy/Services/KSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Sessions',
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "service_sid": "KSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "status": "in-progess",
                "unique_name": "unique_name",
                "start_time": "2015-07-30T20:00:00Z",
                "links": {
                    "interactions": "https://preview.twilio.com/Proxy/Services/KSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Sessions/KCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Interactions",
                    "participants": "https://preview.twilio.com/Proxy/Services/KSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Sessions/KCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants"
                },
                "ttl": 100,
                "date_updated": "2015-07-30T20:00:00Z",
                "date_created": "2015-07-30T20:00:00Z",
                "end_time": "2015-07-30T20:00:00Z",
                "url": "https://preview.twilio.com/Proxy/Services/KSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Sessions/KCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "sid": "KCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.preview.proxy.services(sid="KSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                          .sessions.create()

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.preview.proxy.services(sid="KSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .sessions(sid="KCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://preview.twilio.com/Proxy/Services/KSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Sessions/KCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.preview.proxy.services(sid="KSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                          .sessions(sid="KCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.assertTrue(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.preview.proxy.services(sid="KSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .sessions(sid="KCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://preview.twilio.com/Proxy/Services/KSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Sessions/KCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "service_sid": "KSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "status": "in-progess",
                "unique_name": "unique_name",
                "start_time": "2015-07-30T20:00:00Z",
                "links": {
                    "interactions": "https://preview.twilio.com/Proxy/Services/KSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Sessions/KCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Interactions",
                    "participants": "https://preview.twilio.com/Proxy/Services/KSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Sessions/KCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants"
                },
                "ttl": 100,
                "date_updated": "2015-07-30T20:00:00Z",
                "date_created": "2015-07-30T20:00:00Z",
                "end_time": "2015-07-30T20:00:00Z",
                "url": "https://preview.twilio.com/Proxy/Services/KSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Sessions/KCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "sid": "KCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.preview.proxy.services(sid="KSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                          .sessions(sid="KCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.assertIsNotNone(actual)
