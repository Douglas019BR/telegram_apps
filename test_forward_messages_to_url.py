from unittest.mock import MagicMock
import pytest
from forward_messages_to_url import handle_new_message, main
import forward_messages_to_url
from pytest_mock import mocker
from unittest.mock import AsyncMock


GROUP_ID = 123
API_ID = 123456
API_HASH = "your_api_hash"
ENDPOINT_URL = "your_endpoint_url"


@pytest.fixture()
def mocked_requests(mocker):
    return mocker.patch("forward_messages_to_url.requests.post")


@pytest.fixture
def mock_event():
    event = MagicMock()
    event.sender = "TestSender"
    event.message.text = "Test message"
    event.chat_id = GROUP_ID
    return event


@pytest.fixture
def mock_response_200():
    response = MagicMock()
    response.status_code = 200
    return response


@pytest.fixture
def mock_response_error():
    response = MagicMock()
    response.status_code = 500
    return response


@pytest.fixture(autouse=True)
def mocked_group_id():
    setattr(forward_messages_to_url, "group_id", GROUP_ID)


@pytest.fixture(autouse=True)
def mocked_api_id():
    setattr(forward_messages_to_url, "api_id", API_ID)


@pytest.fixture(autouse=True)
def mocked_api_hash():
    setattr(forward_messages_to_url, "api_hash", API_HASH)


@pytest.fixture(autouse=True)
def mocked_endpoint_url():
    setattr(forward_messages_to_url, "endpoint_url", ENDPOINT_URL)


@pytest.fixture()
def mocked_telegram_client_connect(mocker):
    return mocker.patch(
        "forward_messages_to_url.TelegramClient.connect", new_callable=AsyncMock
    )


@pytest.fixture()
def mocked_telegram_client_start(mocker):
    return mocker.patch(
        "forward_messages_to_url.TelegramClient.start", new_callable=AsyncMock
    )


@pytest.fixture()
def mocked_telegram_client_run_until_disconnected(mocker):
    return mocker.patch(
        "forward_messages_to_url.TelegramClient.run_until_disconnected",
        return_value=None,
        new_callable=AsyncMock,
    )


@pytest.mark.asyncio
async def test_handle_new_message_success(
    mocked_group_id, mocked_requests, mock_event, mock_response_200
):
    mocked_requests.return_value = mock_response_200
    await handle_new_message(mock_event)
    mocked_requests.assert_called_once_with(
        "your_endpoint_url", json={"message": "Test message"}
    )


@pytest.mark.asyncio
async def test_handle_new_message_error(
    mocked_group_id, mocked_requests, mock_event, mock_response_error
):
    mocked_requests.return_value = mock_response_error
    await handle_new_message(mock_event)
    mocked_requests.assert_called_once_with(
        "your_endpoint_url", json={"message": "Test message"}
    )


@pytest.mark.asyncio
async def test_handle_new_message_error_without_request_response(
    mocked_group_id, mocked_requests, mock_event
):
    mocked_requests.return_value = "error string!"
    await handle_new_message(mock_event)
    mocked_requests.assert_called_once_with(
        "your_endpoint_url", json={"message": "Test message"}
    )


@pytest.mark.asyncio
async def test_telegram_connection(
    mocked_telegram_client_connect,
    mocked_telegram_client_start,
    mocked_telegram_client_run_until_disconnected,
):
    await main()
    mocked_telegram_client_connect.assert_called_once()
    mocked_telegram_client_start.assert_called_once()
    mocked_telegram_client_run_until_disconnected.assert_called_once()
