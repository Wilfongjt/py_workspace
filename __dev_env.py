import os
from pprint import pprint

class DevEnv():
    # load from file .env

    def __init__(self, folder=os.getcwd(),filename='.env'):
        # by default: put .env in calling folder
        self.folder = folder
        self.filename = filename
        self.prefixList = ['GH_','WS_']
        if not self.exists():
            self.save()
    def show(self):
        print('DevEnv:')
        print('* folder : ', self.folder)
        print('* file   : ', self.filename)
        print('* values : ', self.collect())
        #print('* environment: ', os.environ)
        return self

    def upsert(self, values):
        # values is a dict
        # some values may have changed

        for p in values:
            os.environ[p] = values[p]
        return self

    def getDefaults(self):
        # define intial state for environment
        dflts = {
            'WS_ORGANIZATION': 'TBD',
            'WS_WORKSPACE': 'TBD',
            'GH_USER': 'TBD',
            'GH_PROJECT': 'TBD',
            'GH_BRANCH': 'TBD'
        }
        return dflts

    def exists(self):
        return os.path.isfile('{}/{}'.format(self.folder, self.filename))

    def open(self):
        # .env -> environment

        with open('{}/{}'.format(self.folder,self.filename)) as file:
            lines = file.readlines()
            for ln in lines:
                if not ln.startswith('#'):
                    ln = ln.split('=')
                    # put into environment
                    if len(ln) == 2:
                        os.environ[ln[0]] = ln[1].strip('\n')

        return self

    def save(self):

        #print('saving')
        # get fresh values from environment

        # initialize file with default param-values when .env NF
        # collect param-values from environment when .env is found
        # convert json to lines
        # write lines to .env file
        # return self

        env = self.collect()  # get current env-vars or defaults
        # should have all the file values at this point
        #print('save 2')
        #pprint(env)
        # convert json to lines
        lines = []
        for e in env:
            ln = '{}={}'.format(e,env[e])
            lines.append(ln)
            # print('env ln', ln)

        with open('{}/{}'.format(self.folder, self.filename), 'w') as f:
            f.writelines(['{}\n'.format(ln) for ln in lines])

        return self

    def collect(self):
        # Collect environment variables when var-name starts with prefixList
        # Collect default variables when environment variables not found
        cllct = {}
        #cllct = self.getDefaults()
        # update from memory
        for e in os.environ:
            for p in self.prefixList:
                #print('e', e, 'p',p)
                if e.startswith(p):
                    cllct[e] = os.environ[e]
        #if not cllct:
        #    cllct = self.getDefaults()
        return cllct

def main():
    srcFolder = os.getcwd()
    print('srcFolder')
    dstFolder = '{}/temp'.format(srcFolder)
    actual = DevEnv(dstFolder,'.env')
    assert ( actual)
    assert ( actual.exists())
    assert ( actual.collect() == {})

    #print('A actual.collect ', actual.collect())
    assert ( actual.open())
    assert ( actual.collect() != {})

    #print('B actual.collect ', actual.collect())


if __name__ == "__main__":
    # execute as script
    main()