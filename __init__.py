import playground
from .protocol import SecureClientFactory,SecureServerFactory
secureConnector = playground.Connector(protocolStack=(SecureClientFactory(),SecureServerFactory()))

playground.setConnector("Crap",secureConnector)
#playground.setConnector("mystack", PassthroughConnector)
#playground.setConnector("passthrough",PassthroughConnector)
