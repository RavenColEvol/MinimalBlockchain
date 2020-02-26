from Blockchain import Blockchain

Bitcoin = Blockchain()
Bitcoin.add_block(12)
Bitcoin.add_block(13)
Bitcoin.view_blockchain()
Bitcoin.add_block(14)
# Edited
Bitcoin.blocks[1].hash = 'abcd'
Bitcoin.add_block(15)