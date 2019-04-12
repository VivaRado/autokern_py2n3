import os
#
from Autokern import Autokern
from AutokernSettings import AutokernSettings
import tfs.common.TFSProject as TFSProject
from tfs.common.TFSMap import TFSMap
#
curdir = os.path.dirname(os.path.realpath(__file__))
pardir = os.path.abspath(os.path.join(curdir,".."))
#
print(pardir)
#
pseudo_argv = ('--ufo-src-path',
				os.path.join(pardir,'advent_pro','advent_pro_thn.ufo'),
				'--ufo-dst-path',
				os.path.join(pardir,'advent_pro','advent_pro_thn_flat_kern.ufo'),
				'--min-distance-ems',
				'0.05',
				'--max-distance-ems',
				'0.1',
				'--max-x-extrema-overlap-ems',
				'0.1',
				'--intrusion-tolerance-ems',
				'0.4',
				'--precision-ems',
				'0.02',
				#'--log-path',
				#os.path.join(pardir,'logs','log'),
				#'--log-basic-pairs',
				#'--write-kerning-pair-logs',
				)

print ('pseudo_argv', ' '.join([str(arg) for arg in pseudo_argv]))

autokernArgs = TFSMap()

AutokernSettings(autokernArgs).getCommandLineSettings(*pseudo_argv)
autokern = Autokern(autokernArgs)
autokern.process()

print ('complete.')
