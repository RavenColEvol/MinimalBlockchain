import hashlib
import datetime
class Block():
    '''
        @params(index, timestamp, data, previous_hash)
    '''
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hashing()

    def hashing(self):
        key = hashlib.sha256()
        key.update(str(self.index).encode('utf-8'))
        key.update(str(self.timestamp).encode('utf-8'))
        key.update(str(self.data).encode('utf-8'))
        key.update(str(self.previous_hash).encode('utf-8'))
        return key.hexdigest()


class Blockchain():
    '''
        What is Blockchain ?
        Ans:
            Blockchain is a distributed database existing on multiple
            computers and everything is saved in forms of block.
    '''
    def __init__(self):
        self.blocks = [self.get_genesis_block()]

    def get_genesis_block(self):
        return Block(0,
                    datetime.datetime.utcnow(),
                    0,
                    100)

    def add_block(self, data):
        self.verify()
        LastBlock = self.get_last_block()
        self.blocks.append(
            Block(LastBlock.index + 1,
                  datetime.datetime.utcnow(),
                  data,
                  LastBlock.hash)
        )

    def get_last_block(self):
        return self.blocks[-1]

    def get_chain_size(self):
        return len(self.blocks) - 1

    def verify(self, verbose = True):
        flag = True
        for i in range(1, self.get_chain_size()):
            if self.blocks[i].index != i:
                flag = False
                print('Index Fail at block {}'.format(i-1))
                break
            if self.blocks[i-1].hash != self.blocks[i].previous_hash:
                flag = False
                print('Hash Fail at block {}'.format(i-1))
                break
        return flag

    def view_blockchain(self):
        for i in self.blocks:
            print(i.index, i.data, i.hash, i.previous_hash)