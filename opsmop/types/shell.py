from opsmop.core.field import Field
from opsmop.core.fields import Fields
from opsmop.types.type import Type

class Shell(Type):

    """
    Represents a command to (maybe) be run
    """

    def __init__(self, cmd=None, **kwargs):
        self.setup(cmd=cmd, **kwargs)

    def fields(self):
        return Fields(
            self,
            cmd      = Field(kind=str, default=None, help="execute this shell code in the default shell"),
            timeout  = Field(kind=int, default=99999, help="max time to allow this command to run") 
        )

    def validate(self):
        # v = Validators(self)
        # FIXME: add this back when we add the 'script' feature
        # v.mutually_exclusive(['cmd', 'script'])
        # v.required_one_of(['cmd', 'script'])
        # v.path_exists(self.script)
        pass

    def default_provider(self):
        from opsmop.providers.shell import Shell
        return Shell
