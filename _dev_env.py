import os
from pprint import pprint

class DevEnv(dict):
    # load from file .env
    #

    def __init__(self, folder=os.getcwd(),filename='.env'):
        # by default: put .env in calling folder
        self.folder = folder
        self.filename = filename
        self.prefixList = ['GH_','WS_']
        #self.initialize()

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
        # merge any values from the environment an previous runs
        for e in dflts:
            if e in os.environ:
                dflts[e] = os.environ[e]

        return dflts

    def file_exists(self):
        exists = os.path.isfile('{}/{}'.format(self.folder, self.filename))
        return exists

    def open(self):
        #self.folder = folder
        #self.filename = filename
        if not self.file_exists():
            self.save()

        with open('{}/{}'.format(self.folder,self.filename)) as file:
            lines = file.readlines()
            for ln in lines:
                if not ln.startswith('#'):
                    ln = ln.split('=')

                    if len(ln) == 2:
                        os.environ[ln[0]] = ln[1].strip('\n')

        return self

    #def save(self, initialization_values=None):
    def save(self):

        #print('saving')
        # get fresh values from environment

        # initialize file with default param-values when .env NF
        # collect param-values from environment when .env is found
        # convert json to lines
        # write lines to .env file
        # return self
        #if initialization_values:
        #    env = initialization_values # collect defaults merged with enviroment
        #else:
        #    env = self.collect() # just the environment

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
        cllct = {}
        for e in os.environ:
            for p in self.prefixList:
                #print('e', e, 'p',p)
                if e.startswith(p):
                    cllct[e] = os.environ[e]
        if not cllct:
            cllct = self.getDefaults()
        return cllct

def main():

    print('DevEnv', DevEnv())
    assert (DevEnv() == {})

    print('DevEnv.open', DevEnv().open().save())
    print('DevEnv.open.collect', DevEnv().open().collect())


if __name__ == "__main__":
    # execute as script
    main()