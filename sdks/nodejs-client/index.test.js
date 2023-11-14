import { ChatbotClient, BASE_URL, routes } from ".";

import axios from 'axios'

jest.mock('axios')

describe('Client', () => {
  let chatbotClient
  beforeEach(() => {
    chatbotClient = new ChatbotClient('test')
  })

  test('should create a client', () => {
    expect(chatbotClient).toBeDefined();
  })
  // test updateApiKey
  test('should update the api key', () => {
    chatbotClient.updateApiKey('test2');
    expect(chatbotClient.apiKey).toBe('test2');
  })
});

describe('Send Requests', () => {
  let chatbotClient

  beforeEach(() => {
    chatbotClient = new ChatbotClient('test')
  })

  afterEach(() => {
    jest.resetAllMocks()
  })

  it('should make a successful request to the application parameter', async () => {
    const method = 'GET'
    const endpoint = routes.application.url
    const expectedResponse = { data: 'response' }
    axios.mockResolvedValue(expectedResponse)

    await chatbotClient.sendRequest(method, endpoint)

    expect(axios).toHaveBeenCalledWith({
      method,
      url: `${BASE_URL}${endpoint}`,
      data: null,
      params: null,
      headers: {
        Authorization: `Bearer ${chatbotClient.apiKey}`,
        'Content-Type': 'application/json',
      },
      responseType: 'json',
    })

  })

  it('should handle errors from the API', async () => {
    const method = 'GET'
    const endpoint = '/test-endpoint'
    const errorMessage = 'Request failed with status code 404'
    axios.mockRejectedValue(new Error(errorMessage))

    await expect(chatbotClient.sendRequest(method, endpoint)).rejects.toThrow(
      errorMessage
    )
  })
})